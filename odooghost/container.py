import typing as t
from functools import reduce

from docker.models.containers import _create_container_args

from odooghost import constant
from odooghost.context import ctx

Attrs = t.Dict[str, t.Any]


def get_container_name(container):
    if not container.get("Name") and not container.get("Names"):
        return None
    # inspect
    if "Name" in container:
        return container["Name"]
    # ps
    shortest_name = min(container["Names"], key=lambda n: len(n.split("/")))
    return shortest_name.split("/")[-1]


class Container:
    """
    Represents a Docker container, constructed from the output of
    GET /containers/:id:/json.
    """

    def __init__(self, attrs: Attrs, has_been_inspected: bool = False):
        self.client = ctx.docker.api
        self.attrs = attrs
        self.has_been_inspected = has_been_inspected

    @classmethod
    def from_ps(cls, attrs: Attrs, **kwargs) -> "Container":
        name = get_container_name(attrs)
        if name is None:
            return None

        new_attrs = {
            "Id": attrs["Id"],
            "Image": attrs["Image"],
            "Name": "/" + name,
        }
        return cls(new_attrs, **kwargs)

    @classmethod
    def from_id(cls, id) -> "Container":
        return cls(ctx.docker.api.inspect_container(id), has_been_inspected=True)

    @classmethod
    def create(cls, **options) -> "Container":
        options["version"] = ctx.docker.api._version
        create_kw = _create_container_args(**options)
        response = ctx.docker.api.create_container(**create_kw)
        return cls.from_id(response["Id"])

    def reload(self) -> None:
        self.attrs = {}
        self.has_been_inspected = False

    def inspect(self) -> Attrs:
        self.attrs = self.client.inspect_container(self.id)
        self.has_been_inspected = True
        return self.attrs

    def inspect_if_not_inspected(self) -> None:
        if not self.has_been_inspected:
            self.inspect()

    def get(self, key: str) -> t.Any:
        self.inspect_if_not_inspected()

        def get_value(attrs, key):
            return (attrs or {}).get(key)

        return reduce(get_value, key.split("."), self.attrs)

    def start(self, **options) -> None:
        return self.client.start(self.id, **options)

    def stop(self, **options):
        return self.client.stop(self.id, **options)

    def kill(self, **options):
        return self.client.kill(self.id, **options)

    def restart(self, **options):
        return self.client.restart(self.id, **options)

    def remove(self, **options):
        return self.client.remove_container(self.id, **options)

    def create_exec(self, command, **options):
        return self.client.exec_create(self.id, command, **options)

    def start_exec(self, exec_id, **options):
        return self.client.exec_start(exec_id, **options)

    def wait(self):
        return self.client.wait(self.id).get("StatusCode", 127)

    def attach(self, *args, **kwargs):
        return self.client.attach(self.id, *args, **kwargs)

    def logs(self, *args, **kwargs):
        return self.client.logs(self.id, *args, **kwargs)

    def get_local_port(self, port: int, protocol: t.Literal["tcp", "udp"] = "tcp"):
        port = self.ports.get("{}/{}".format(port, protocol))
        return "{HostIp}:{HostPort}".format(**port[0]) if port else None

    @property
    def id(self) -> str:
        return self.attrs["Id"]

    @property
    def image(self) -> str:
        return self.attrs["Image"]

    @property
    def image_config(self) -> dict:
        return self.client.inspect_image(self.image)

    @property
    def name(self) -> str:
        return self.attrs["Name"][1:]

    @property
    def stack(self):
        return self.labels.get(constant.LABEL_STACKNAME)

    @property
    def service(self):
        return self.labels.get(constant.LABEL_STACK_SERVICE_TYPE)

    @property
    def labels(self) -> dict[str, str]:
        return self.get("Config.Labels") or {}

    @property
    def ports(self) -> dict:
        return self.get("NetworkSettings.Ports") or {}

    @property
    def stop_signal(self) -> t.Optional[str]:
        return self.get("Config.StopSignal")

    @property
    def exit_code(self) -> int:
        return self.get("State.ExitCode")

    @property
    def is_running(self) -> bool:
        return self.get("State.Running")

    @property
    def is_restarting(self) -> bool:
        return self.get("State.Restarting")

    @property
    def is_paused(self) -> bool:
        return self.get("State.Paused")

    def __repr__(self):
        return "<Container: {} ({})>".format(self.name, self.id)

    def __eq__(self, other: "Container") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id

    def __hash__(self) -> str:
        return self.id.__hash__()
