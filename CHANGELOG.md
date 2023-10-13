# CHANGELOG



## v0.1.1 (2023-10-13)

### Fix

* fix(pyproject.toml): add &#34;merge&#34; as an allowed tag in the commit message convention to indicate merge commits ([`3374fcf`](https://github.com/remyz17/odooghost/commit/3374fcff00ad2e11d065d47a3ef8b3ceec2a14ce))


## v0.1.0 (2023-10-13)

### Chore

* chore(README.md): add badges for linting, testing, and deploy documentation workflows to provide visibility and status of the project&#39;s CI/CD pipelines ([`e893e18`](https://github.com/remyz17/odooghost/commit/e893e18258fd49765c3c8c7fd2ac98318d13e0f4))

* chore: bump deps ([`030038d`](https://github.com/remyz17/odooghost/commit/030038d25849b0bcf0fcb2b2069bc35a0b082385))

* chore(base.py): change default value of no_cache parameter in build_image() method to True for better performance
chore(base.py): change default value of no_cache parameter in build() method to True for better performance
chore(base.py): change rm parameter to False and add forcerm=True in build_image() method to prevent removing intermediate containers ([`70206cd`](https://github.com/remyz17/odooghost/commit/70206cdbaea65aafd5d496775372afa73b419f5c))

* chore(exemple-stack.yml): rename &#39;postgres&#39; service to &#39;db&#39; for better clarity and consistency ([`c825d5c`](https://github.com/remyz17/odooghost/commit/c825d5c00d07cf1cbe316b27aea08419af8753fb))

* chore: bump deps ([`f0174ec`](https://github.com/remyz17/odooghost/commit/f0174ecb80d6828a83aa0784697529f8003fb9c4))

* chore(Dockerfile.j2): refactor pip dependencies installation to use a single command for improved readability and maintainability
feat(Dockerfile.j2): add support for copying addons to the container by creating a directory and setting ownership before copying the addons ([`2d07fc6`](https://github.com/remyz17/odooghost/commit/2d07fc613ebeea2c69d365ad8b5165070eac6638))

* chore(stack.py): remove unused `ensure_addons` method
feat(stack.py): add support for `ensure_addons` parameter in `create` method to control whether to ensure addons or not during stack creation ([`f857428`](https://github.com/remyz17/odooghost/commit/f857428c8547384cfc4483fb3c142adbfb46e745))

* chore(package.json): update dependencies and devDependencies

- Update `pinia` dependency from version `2.1.3` to `2.1.6`
- Add new dependencies:
  - `@headlessui/vue` version `1.7.16`
  - `@heroicons/vue` version `2.0.18`
  - `@tailwindcss/forms` version `0.5.5`
- Update `vue` dependency from version `3.3.4` to `3.3.4`
- Update `vue-router` dependency from version `4.2.2` to `4.2.4`
- Update devDependencies:
  - `@rushstack/eslint-patch` from version `1.2.0` to `1.3.3`
  - `@vitejs/plugin-vue` from version `4.2.3` to `4.3.3`
  - `@vue/test-utils` from version `2.3.2` to `2.4.1`
  - `autoprefixer` from version `10.4.14` to `10.4.15`
  - `eslint` from version `8.39.0` to `8.48.0`
  - `eslint-plugin-vue` from version `9.11.0` to `9.17.0`
  - `postcss` from version `8.4.26` to `8.4.28`
  - `vite` from version `4.3.9` to `4.4.9`
  - `vitest` from version `0.32.0` to `0.32.4`

The dependencies and devDependencies were updated to their latest versions to ensure compatibility and take advantage of bug fixes and new features. ([`08bcadf`](https://github.com/remyz17/odooghost/commit/08bcadf0c597ffa55ad97165db6a135c3d0dbddf))

* chore(jsconfig.json): add jsconfig.json file to configure TypeScript compiler options and path aliases for better module resolution and development experience ([`fde6751`](https://github.com/remyz17/odooghost/commit/fde675178ec863111808c02e425ba3f99bf26b84))

* chore(.editorconfig): update file extensions to include .vue, .js, and .cjs files for consistent indentation style ([`a23500c`](https://github.com/remyz17/odooghost/commit/a23500c78b2bac09067162a7118b5c33e65cc882))

* chore(config.py): move ContextConfig from context
feat(context.py): add StackConfigManager class to manage stack configurations ([`d60ab77`](https://github.com/remyz17/odooghost/commit/d60ab775043c14815d5a1b46a3379da5cca23014))

* chore: update dependencies ([`f17efa2`](https://github.com/remyz17/odooghost/commit/f17efa28ac1a7193803406a33eac5f10e8250d36))

* chore: replace flake8 with ruff

- Add ruff configuration with src set to [&#34;odooghost&#34;, &#34;tests&#34;], ignore set to [&#34;E501&#34;, &#34;E203&#34;], and line-length set to 88 ([`aa7177d`](https://github.com/remyz17/odooghost/commit/aa7177ddf241c58a88372f48c8ab7e9ea72a40bc))

* chore(stack.py): add docstrings to Stack class and its methods for better code documentation ([`a2d11b5`](https://github.com/remyz17/odooghost/commit/a2d11b55285f95c6316ec8b08557fdaf98f7e92e))

* chore(stack.py): add logging statements to improve visibility during stack creation and dropping
feat(stack.py): add optional parameters to the start method for detaching and opening browser ([`f7b2df0`](https://github.com/remyz17/odooghost/commit/f7b2df069e9849258078a14daecd697304293419))

* chore(reference.md): add configuration options for odooghost.context, odooghost.renderer, and odooghost.logger to show root heading
docs(__init__.py): update package description for OdooGhost
docs(context.py): add docstrings to Context class and its methods for better code documentation ([`0016fbb`](https://github.com/remyz17/odooghost/commit/0016fbb66ebb8b807f6c479b172bf6a49fdaa62d))

* chore(README.md): update project description and features for clarity and readability ([`3557823`](https://github.com/remyz17/odooghost/commit/3557823f85a4e7692f3a551c5d2683280a7bb630))

* chore(README.md): fix typo in the word &#34;development&#34; to improve readability and consistency ([`47ecb73`](https://github.com/remyz17/odooghost/commit/47ecb73f01b1a675ad4e8aaa0bee2115257957c9))

* chore(README.md): update project description and add features section
docs(README.md): add installation instructions and contribute section ([`a3c4ce8`](https://github.com/remyz17/odooghost/commit/a3c4ce87f61d4a260072f5ecbcea2050784cbc94))

* chore(constant.py): refactor constant names for improved readability and consistency
feat(constant.py): add new constant LABEL_STACK_SERVICE_TYPE to represent the stack type of odooghost ([`fc93ec9`](https://github.com/remyz17/odooghost/commit/fc93ec94c0f81f7ae6444d39ceb85ed8b8b8b44f))

* chore(odoo.py): change logger.debug to logger.info to provide more informative log message during image building process
chore(postgres.py): change logger.debug to logger.warn to indicate that the postgres image is being skipped because it&#39;s of remote type ([`2c0ca86`](https://github.com/remyz17/odooghost/commit/2c0ca86602a91091d24558d864ce0eeae16af03c))

* chore: bump deps ([`d5209c3`](https://github.com/remyz17/odooghost/commit/d5209c33824841b94368afc53f4a35cb3e3e6074))

* chore(lint.yaml): add linting workflow to the project to ensure code quality and consistency
feat(Makefile): add Makefile with formatting and linting targets for code quality and consistency ([`d7f2a39`](https://github.com/remyz17/odooghost/commit/d7f2a39e8c77ae181736c4165dc2e585cc5bdb86))

* chore(Dockerfile.j2): switch to root user to install apt dependencies and switch back to odoo user afterwards ([`4cffa80`](https://github.com/remyz17/odooghost/commit/4cffa80659643e3c64bbc23fba95bda63dfb0986))

* chore(base.py): add logging statement to ensure_base_image method for debugging purposes
fix(base.py): fix references to base_image_tag property in ensure_base_image method to ensure correct image is pulled and logged ([`1e915c1`](https://github.com/remyz17/odooghost/commit/1e915c1e61721702640dab62b9d7472dd04b5909))

* chore(constant.py): add SRC_DIR constant to store the absolute path of the current file&#39;s parent directory
feat(constant.py): add LABEL_STACKNAME constant to store the label for the stackname in the application ([`42d7cbd`](https://github.com/remyz17/odooghost/commit/42d7cbd046cb7c3a6a4e056d46b2fc4aaf7ceeee))

* chore(pyproject.toml): add Jinja2 dependency to support template rendering in the project ([`a86eaa9`](https://github.com/remyz17/odooghost/commit/a86eaa9e68af3e55c542d6b5b3ec3b234dac8208))

* chore(pyproject.toml): add docker package as a dependency to enable Docker integration
chore(pyproject.toml): fix formatting of isort profile key for consistency
chore(pyproject.toml): update bandit configuration to exclude &#34;tests&#34; directory from scanning ([`8d89bf6`](https://github.com/remyz17/odooghost/commit/8d89bf6a6f5fad2275a714aef472f1d9f0373678))

* chore(pyproject.toml): add pydantic package with dotenv extras to enable environment variable support in the application
chore(pyproject.toml): update isort dependency to version 5.12.0 for linting purposes ([`a23d05a`](https://github.com/remyz17/odooghost/commit/a23d05af82c31fee9da2ead8d9f5b8f4125d4dd1))

* chore(__init__.py): add version number 0.1.0 to the package
feat(constant.py): add constant APP_DIR to store the path to the application directory for odooghost ([`4781438`](https://github.com/remyz17/odooghost/commit/4781438493ab64b8101fd1a3ea43d5cbfa0e2fda))

* chore: Add base VueJS app ([`77094c9`](https://github.com/remyz17/odooghost/commit/77094c94fbcdff9cd37dd1f9a9227f5670179752))

* chore: add .editorconfig file to enforce consistent coding style across the project
add .flake8 file to configure flake8 linter with project-specific settings
add .pre-commit-config.yaml file to configure pre-commit hooks for automated checks
update pyproject.toml with project metadata and dependencies
configure isort, black, flake8, and mypy in pyproject.toml for linting and formatting
configure pytest and bandit in pyproject.toml for testing and security analysis ([`c329830`](https://github.com/remyz17/odooghost/commit/c32983004250288a780d33ba37c09edcf941a6cf))

* chore(README.md): add initial README content for OdooGhost project ([`27b72ac`](https://github.com/remyz17/odooghost/commit/27b72ac5f05cbe9bb12b5a9b96fc9d4967066b19))

* chore: add initial project files and structure

Add the following files to the project:
- README.md
- odooghost/__init__.py
- pyproject.toml
- tests/__init__.py

This commit sets up the initial project structure and configuration files. The README.md file will be used to provide information about the project. The odooghost/__init__.py file is the main entry point for the project. The pyproject.toml file is used for project configuration and dependency management using Poetry. The tests/__init__.py file is added to the project to provide a starting point for writing tests. ([`d2f4aab`](https://github.com/remyz17/odooghost/commit/d2f4aab3d29210b6a9725385d6c1c7ca1716a709))

### Ci

* ci(stack.py): fix CI ([`7b7a041`](https://github.com/remyz17/odooghost/commit/7b7a041cb1e433ebe45d6caeaacc081a95c90014))

### Documentation

* docs(services): Add docstring to config property ([`1773ef6`](https://github.com/remyz17/odooghost/commit/1773ef6ee9c07ecb3112c262421e09012a292d15))

* docs(reference.md): add odooghost.services section to the reference documentation to provide information about the services module
odooghost/services/__init__.py: rename imported module &#39;base&#39; instead of &#39;odoo&#39; to improve clarity and consistency in the codebase ([`1043d88`](https://github.com/remyz17/odooghost/commit/1043d88f9a7084949f4e04f6982a3f6b5d438296))

* docs(index.md): Update project overview and features section to provide a clear description of OdooGhost and its capabilities
docs(index.md): Add installation instructions to guide users on how to get started with OdooGhost
docs(index.md): Include usage instructions for initial setup and crafting a stack
docs(index.md): Add contribute section to encourage community contributions
docs(index.md): Include license information for the project
docs(tutorials.md): Update tutorials section to provide detailed information on managing Odoo stacks with CLI commands ([`e3f7120`](https://github.com/remyz17/odooghost/commit/e3f71200959a7642a7c8037f6753a0df8e927518))

* docs(reference.md): add odooghost.stack and odooghost.renderer sections to the reference documentation to provide information about these features ([`8742bb9`](https://github.com/remyz17/odooghost/commit/8742bb9903e6b7fcd3404db82a5a9ffe75c4eed1))

* docs(README.md): update link to stack configuration file samples in the README to point to the correct location
feat(exemple-stack.yml): add an example stack configuration file with Odoo and Postgres configurations ([`fe0a200`](https://github.com/remyz17/odooghost/commit/fe0a20038c5e3d2695bb9d03887a12cb36e3c3a7))

* docs(README.md): update contribution guidelines to encourage Pull Requests and express appreciation for contributions ([`4bdc122`](https://github.com/remyz17/odooghost/commit/4bdc12209c3144e6d938494cd48fc5e25191dd5e))

### Feature

* feat(pyproject.toml): configure semantic-release settings for automatic versioning and changelog generation ([`cf41523`](https://github.com/remyz17/odooghost/commit/cf415231aac0753ee5b98a63fa8566eca0fd1537))

* feat(stack.py): add support for force recreate of dangling containers in Stack.create method to provide more flexibility in container creation
feat(stack.py): add support for do_pull parameter in Stack.create method to allow pulling of base images to be optional
feat(odoo.py): add support for force and do_pull parameters in OdooService.create method to align with changes in BaseService.create method
fix(base.py): modify BaseService.create method to handle force recreate of dangling containers and optional pulling of base images
fix(root.py): modify create function to pass force and do_pull parameters to Stack.create method and align with changes in OdooService.create method ([`9b8c7f5`](https://github.com/remyz17/odooghost/commit/9b8c7f5fba63714e9bff753fbea08db1d83efb75))

* feat(cli): add &#39;logs&#39; command to stream logs from a stack
feat(container.py): add optional parameters to &#39;stream_logs&#39; method to allow specifying tail and follow options ([`1fbbc9b`](https://github.com/remyz17/odooghost/commit/1fbbc9b673683882d0701780e5cf999a9dc53e59))

* feat(services): add new abstractmethod _get_environment() and use it for container _get_environment
This way Odoo service can get informations from DB service and build it&#39;s environment ([`3de4911`](https://github.com/remyz17/odooghost/commit/3de491185622452ff5246378d03d7a3d33cdad63))

* feat(config.py): add new methods get_service_hostname() and get_network_name() to StackConfig class for better service and network name handling ([`ceaf0c0`](https://github.com/remyz17/odooghost/commit/ceaf0c083bc043693985995dfc5dbf8c8b075f55))

* feat(odooghost/addons.py): add methods to get addons configurations, addons paths, and validate addons paths
feat(odooghost/services/base.py): add methods to prepare and clean build context, get service labels, ensure base image, build service image, drop service image, create and drop service volumes, list service containers, create and drop service containers, get service container, start service container, build service, create service, drop service, add properties for base image tag, image tag, and custom image existence, add properties for volume name, container name, container hostname, and build context path ([`1c94a49`](https://github.com/remyz17/odooghost/commit/1c94a49fb7207b1e114ccd327db64b6993754dfe))

* feat(reference.md): add odooghost.context section to provide additional context information ([`f08daf6`](https://github.com/remyz17/odooghost/commit/f08daf6e4ce887211a28b6770f70aa89f8e2a5f6))

* feat(Dockerfile.j2): add support for mounting Python dependency files and installing them using pip
feat(Dockerfile.j2): add support for mounting additional addons from the host machine ([`692e805`](https://github.com/remyz17/odooghost/commit/692e80598132051edfbc8cd2611aef0b5822b5d4))

* feat(misc.py): add function to generate a hash of a given string using MD5 algorithm for data integrity purposes ([`3aa16e6`](https://github.com/remyz17/odooghost/commit/3aa16e60f5cba46b79055e6c7431d6938d179bc8))

* feat(renderer.py): improve flexibility of render_dockerfile function by accepting keyword arguments instead of specific arguments ([`cf1df15`](https://github.com/remyz17/odooghost/commit/cf1df15296d66bd7c264674b978921fbf1b1363d))

* feat(web): add GraphQL API support to the web application

- Add new files `odooghost/web/api/__init__.py` and `odooghost/web/api/schema.py` to define the GraphQL schema and query.
- Implement a `hello` query in the GraphQL schema that returns the string &#34;world&#34;.
- Create a new file `odooghost/web/application.py` to define the web application using Starlette.
- Import the GraphQL schema from `odooghost/web/api/schema.py`.
- Create a Starlette application and add routes for `/graphql` and `/graphql` for GraphQL queries and subscriptions.
- Update `pyproject.toml` to include the necessary dependencies `strawberry-graphql` and `uvicorn` for GraphQL support.

The changes were made to add GraphQL API support to the web application, allowing clients to query and subscribe to data using the GraphQL language. ([`8d87a6c`](https://github.com/remyz17/odooghost/commit/8d87a6c55e666946552dd05a0a25610d322dd4fb))

* feat(addons.py): add new file addons.py to manage addons configuration and copying
feat(base.py): add build_context method to prepare and clean build context for building custom images
refactor(base.py, odoo.py): move build_image method to build custom image using Dockerfile in build context
feat(base.py): add build method to build custom image and clean build context
feat(base.py): add build_context_path property to get the path of build context for the service
feat(odoo.py): add _prepare_build_context method to prepare build context for Odoo service ([`c86f77f`](https://github.com/remyz17/odooghost/commit/c86f77f14aa842e5ffee23ea835c33afed8456ea))

* feat(context.py): add method get_build_context_path() to return the path to the build context

The method `get_build_context_path()` is added to the `Context` class in order to retrieve the path to the build context. This method returns a `Path` object representing the path to the build context, which is set to &#34;/tmp/odooghost&#34;. This change is made to improve the code&#39;s readability and maintainability by encapsulating the logic for obtaining the build context path within a dedicated method. ([`5d1177c`](https://github.com/remyz17/odooghost/commit/5d1177c530f1bff200df95bcc44d92ef2d4e0947))

* feat(renderer.py): add support for additional keyword arguments in render_dockerfile function

The render_dockerfile function in renderer.py now accepts additional keyword arguments. This allows for more flexibility and customization when generating a custom dockerfile for the Odoo image. ([`2fd2553`](https://github.com/remyz17/odooghost/commit/2fd25533e5ffebbfbf02b56c7a0975cabc08d28a))

* feat(config.py): add support for specifying python dependencies as a list or as files
chore(config.py): add validation for addons configuration to ensure that local addons path exists and remote addons have defined branch and origin
refactor(exemple-stack.yml): Adapt file looking forward to recent changes in config module ([`4a544af`](https://github.com/remyz17/odooghost/commit/4a544afa952f190b642406b526693aeb24414e9d))

* feat(alerts): add VErrorAlert, VSuccessAlert, and VWarningAlert components

- Add VErrorAlert component to display error alerts with a red color scheme.
- Add VSuccessAlert component to display success alerts with a green color scheme.
- Add VWarningAlert component to display warning alerts with a yellow color scheme.

These components are reusable and can be used to display different types of alerts throughout the application. They accept `title` and `text` props to customize the content of the alerts. The styling of the alerts is defined using Tailwind CSS classes. ([`72e04ee`](https://github.com/remyz17/odooghost/commit/72e04eed0bb3613be58653b8ab9811e369540f3c))

* feat(web): Add basic application shell ([`156361a`](https://github.com/remyz17/odooghost/commit/156361a028b87cf7d2f0d5032d2a325f2dcd8141))

* feat(tailwind.config.cjs): add primary color to the theme to customize the design
feat(tailwind.config.cjs): add @tailwindcss/forms plugin to enable form styling ([`7857e92`](https://github.com/remyz17/odooghost/commit/7857e92eb3d4d8993632e8d362cb589e7a98f0b6))

* feat(web): add favicon and app icons for better branding and user experience
feat(web): add site.webmanifest file to configure web app properties like name, icons, and colors ([`0e5cc5b`](https://github.com/remyz17/odooghost/commit/0e5cc5be697aebebadde4255e61eab069c34a2fb))

* feat(stack.py): add `_ensure_exists` decorator to ensure Stack exists before executing certain methods
feat(stack.py): implement support for running stacks
fix(stack.py): remove redundant check for Stack existence in `drop`, `start`, `stop`, and `restart` methods ([`3d11038`](https://github.com/remyz17/odooghost/commit/3d11038d073e6cf69a1636d28c54765b27d4f650))

* feat(root.py): add support for --detach option to not stream Odoo service logs
feat(root.py): add support for --open option to open Odoo in browser after starting the stack
feat(root.py): add logic to stream Odoo service logs and stop the stack when KeyboardInterrupt is raised ([`639738c`](https://github.com/remyz17/odooghost/commit/639738cc12ad9009bdb0b370961bce9b34a2c544))

* feat(container.py): add method get_subnet_ip to retrieve the IP address of the container&#39;s subnet
feat(container.py): add property networks to retrieve the networks configuration of the container ([`eba67c6`](https://github.com/remyz17/odooghost/commit/eba67c65843c96e72c1119d997c929fe479124db))

* feat(container.py): add search method to Container class to retrieve containers based on filters and stopped status
refactor(services/base.py, stack.py): replace filter and list comprehension with Container.search method to improve code readability and maintainability ([`e504959`](https://github.com/remyz17/odooghost/commit/e504959e6040ae231c18fd9fb62608047def7d1b))

* feat(types.py): add Attrs type definition to represent a dictionary with string keys and any values

The Attrs type definition is added to represent a dictionary with string keys and any values. This will be used to store attributes in the codebase. ([`7c43458`](https://github.com/remyz17/odooghost/commit/7c43458eb3d2378dbbad41ae17fb44b74ee90b7f))

* feat(stack.py): update Stack.from_name() to use the new stack configuration retrieval method
feat(stack.py): update Stack.list() to use the new stack configuration retrieval method
refactor(stack.py): remove unused methods save_config() and reload_config() ([`82253f7`](https://github.com/remyz17/odooghost/commit/82253f79dd30e6641915d06f8871771194fc60ff))

* feat(stack.py): add StackState enum to represent the state of a stack (NONE, PARTIAL, READY)
feat(stack.py): implement _check_state method to determine the state of a stack based on its config file
feat(stack.py): add state property to Stack class to get the current state of a stack
feat(stack.py): implement from_name method to create a Stack instance from a stack name
feat(stack.py): implement list method to list all stacks
feat(stack.py): implement labels method to get the labels of a stack ([`0bd7dfa`](https://github.com/remyz17/odooghost/commit/0bd7dfa1a824621f568b27d861abfe241b41685e))

* feat(config.py): add class method &#39;from_file&#39; to StackConfig to create an instance from a JSON/YAML file
feat(exceptions.py): add StackConfigError class to handle errors related to stack configuration files ([`095f77e`](https://github.com/remyz17/odooghost/commit/095f77e20f4bb8d95b61232b5e8ff2f0238bcbfb))

* feat(docker.py): add stream_container_logs function to stream container logs to a specified stream ([`13422ba`](https://github.com/remyz17/odooghost/commit/13422ba382cc517e77413e0c0269fba35585e9c1))

* feat(stack.py): add support for getting container labels and filtering containers by labels
feat(stack.py): implement start, stop, and restart methods for starting, stopping, and restarting containers in the stack ([`8f0b833`](https://github.com/remyz17/odooghost/commit/8f0b833b759330b7153ee93d06422fa6996a0de0))

* feat(root.py): add start, stop, and restart commands to manage stacks
feat(root.py): add support for timeout option to stop and restart commands ([`e5c8084`](https://github.com/remyz17/odooghost/commit/e5c8084ef3036d77d1f15a376292b19aa6700cd3))

* feat(types.py): add new file types.py to define custom types Filters and Labels

The types.py file is added to the project to define two custom types: Filters and Labels. These types are defined using the typing module from the Python standard library. The Filters type is a dictionary with string keys and string values, while the Labels type is an alias for the Filters type. These types will be used to provide type hints and improve code readability and maintainability. ([`dd84d54`](https://github.com/remyz17/odooghost/commit/dd84d54d61a7e3bb5194b23408711b99ec918dcf))

* feat(exceptions.py): add new custom exceptions for container operations

Add new custom exceptions for container operations to provide more specific error handling and improve code readability. The following exceptions were added:

- StackContainerGetError: Raised when there is an error retrieving a container.
- StackContainerNotFound: Raised when a container is not found.
- StackContainerStartError: Raised when there is an error starting a container. ([`14df53b`](https://github.com/remyz17/odooghost/commit/14df53be22b7e5426f643370aa040a7f307d7e13))

* feat(container.py): add Container class to represent a Docker container and provide methods for interacting with it ([`c84a905`](https://github.com/remyz17/odooghost/commit/c84a905f66132489baca5c3290630296af6ac836))

* feat(config.py): implement version command to print the config version
feat(config.py): implement working_dir command to print the working directory ([`bec7515`](https://github.com/remyz17/odooghost/commit/bec751546c5971e1852019708ec6bc03ede4cf01))

* feat(context.py): add ContextConfig class to hold configuration file data
feat(context.py): add initialize method to load config data from file on context initialization
feat(context.py): add config property to get context config data
fix(context.py): fix setup method to call initialize after setting up config data ([`c09d065`](https://github.com/remyz17/odooghost/commit/c09d0659504f3eb66689aa9bb095329ed748a132))

* feat(docs): add documentation workflow and files

- Add a new workflow file `docs.yaml` to deploy documentation on push to the `main` branch.
- Configure the workflow to run on push events to the `main` branch.
- Add steps to the workflow to checkout the repository, install poetry, setup Python 3.11, install requirements, configure Git, and build the docs.
- Add a new Makefile target `docs-build` to build the documentation using `mkdocs`.
- Add a new Makefile target `docs-deploy` to deploy the documentation using `mkdocs gh-deploy`.
- Add a new Makefile target `clean-docs` to clean the generated documentation files.
- Add a new file `explanation.md` to the `docs` directory, which focuses on providing an understanding-oriented approach to the project documentation.
- Add a new file `how-to-guides.md` to the `docs` directory, which focuses on providing a problem-oriented approach to the project documentation.
- Add a new file `index.md` to the `docs` directory, which serves as the main index page for the project documentation.
- Add a new file `reference.md` to the `docs` directory, which will contain reference information for the project.
- Add a new file `tutorials.md` to the `docs` directory, which focuses on providing a learning-oriented approach to the project documentation.
- Add a new `mkdocs.yml` file to configure the documentation site, including the site name, theme, plugins, navigation, repository URL, and directory URL usage.
- Add dependencies for `mkdocs`, `mkdocs-material`, and `mkdocstrings` to the `docs` section of the `pyproject.toml` file. ([`236b1b2`](https://github.com/remyz17/odooghost/commit/236b1b26e9308b0d310683e2c43feddbbcce9a38))

* feat(test.yaml): add GitHub Actions workflow for testing on pull requests and pushes to the main branch
chore(.gitignore): ignore pytest-related files
feat(Makefile): add targets for running unit tests and generating coverage report
feat(test_version.py): add test for checking the project version ([`9d78dd4`](https://github.com/remyz17/odooghost/commit/9d78dd4d6860b254118d29e875132e5fa8a46f11))

* feat: add example-stack.yml configuration file

This commit adds a new file `example-stack.yml` to the repository. The file includes configuration settings for an example application stack.

The `example-stack.yml` file includes the following configurations:
- `name`: Specifies the name of the example stack.
- `odoo`: Specifies the configuration settings for the Odoo application.
  - `version`: Specifies the version of Odoo to use (16.0).
  - `cmdline`: Specifies additional command line arguments for Odoo (e.g., &#34;--workers=2&#34;).
  - `addons`: Specifies the list of Odoo addons to install.
    - `type`: Specifies the type of addon (remote or local).
    - `origin`: Specifies the origin URL for remote addons.
    - `branch`: Specifies the branch to use for remote addons.
    - `path`: Specifies the local path for local addons.
  - `dependencies`: Specifies the dependencies required by Odoo.
    - `apt`: Specifies the apt packages to install.
    - `python`: Specifies the Python packages to install.
- `postgres`: Specifies the configuration settings for the PostgreSQL database.
  - `type`: Specifies the type of database (local or remote).
  - `version`: Specifies the version of PostgreSQL to use (14).
  - `host`: Specifies the host for remote database (commented out).
  - `user`: Specifies the user for remote database (commented out).
  - `db`: Specifies the database name for remote database (commented out).
  - `password`: Specifies the password for remote database (commented out).

The `example-stack.yml` file serves as a template for configuring an example application stack using Odoo and PostgreSQL. ([`0a5eb7b`](https://github.com/remyz17/odooghost/commit/0a5eb7b09e5aa723b054beb7c8ff9e2875640a7d))

* feat(stack.py): add support for dropping stack and related data
feat(stack.py): add support for dropping volumes when dropping stack
fix(root.py): change drop() command signature to accept stack_configs argument to drop multiple stacks
fix(root.py): update drop() command description to reflect dropping multiple stacks
fix(base.py): add labels_as_list() function to convert labels dictionary to list of strings
fix(base.py): implement drop_image() method in BaseService to drop custom image if exists
fix(base.py): implement drop_volumes() method in BaseService to drop volume if exists
fix(base.py): implement drop_containers() method in BaseService to drop containers with matching labels
fix(base.py): implement drop() method in BaseService to drop containers, volumes, and image
fix(odoo.py): call super() methods in OdooService to inherit drop_image(), drop_volumes(), drop_containers(), and drop() methods from BaseService
fix(postgres.py): call super() methods in PostgresService to inherit drop_image(), drop_volumes(), drop_containers(), and drop() methods from BaseService
fix(stack.py): implement drop() method in Stack class to drop Odoo and Postgres services and log the action ([`540a079`](https://github.com/remyz17/odooghost/commit/540a079541d5299f64905144e221df471d33d901))

* feat(base.py): add drop_image, drop_volumes, drop_container, and drop methods to BaseService
fix(base.py): change logger.debug to logger.info in ensure_base_image method for better logging ([`c296317`](https://github.com/remyz17/odooghost/commit/c2963177c58129069ac8ee13bc96bce8d4e80692))

* feat(base.py): add constructor parameters &#39;name&#39; and &#39;stack_name&#39; to BaseService class to improve code readability and reusability
feat(base.py): add abstract method &#39;_get_container_labels&#39; to BaseService class to provide container labels for odooghost stack and service type
feat(base.py): add abstract methods &#39;create_volumes&#39;, &#39;create_container&#39;, and &#39;create&#39; to BaseService class to define the steps for creating a service
feat(base.py): add properties &#39;volume_name&#39;, &#39;container_name&#39;, and &#39;container_hostname&#39; to BaseService class to provide consistent naming conventions for volumes and containers ([`b91262c`](https://github.com/remyz17/odooghost/commit/b91262c27cd6a51ff7e775d484547d421379b436))

* feat(exceptions.py): add new custom exceptions for network, volume, and container errors

Added new custom exceptions `CommonNetworkEnsureError`, `StackVolumeCreateError`, and `StackContainerCreateError` to handle specific errors related to network, volume, and container operations respectively. These exceptions will be used to provide more specific error messages and improve error handling in the codebase. ([`79a018b`](https://github.com/remyz17/odooghost/commit/79a018bf640328cd30bca2acdd0100fc2689b781))

* feat(constant.py): add COMMON_NETWORK_NAME constant to store the name of the common network used by the application

feat(context.py): add create_common_network() method to create the common network used by the application if it doesn&#39;t exist

feat(context.py): add ensure_common_network() method to ensure that the common network used by the application exists, creating it if necessary ([`eba165d`](https://github.com/remyz17/odooghost/commit/eba165d6c0cf746d9b8e2e4961892c6b1c77c5bb))

* feat(odoo.py): add stack name to image labels ([`264b47f`](https://github.com/remyz17/odooghost/commit/264b47f5c7980da2430a016662ed63485ba4b932))

* feat(utils): add new module `progress_stream` and `stream` to improve stream handling and output formatting

The new module `progress_stream` provides functions for handling progress events in a stream of JSON objects. It includes functions for writing to a stream, streaming output, printing output events, and extracting digests from pull and push events.

The new module `stream` provides functions for handling streams of text or bytes. It includes functions for converting byte streams to text streams, splitting a stream into chunks, and splitting a stream into JSON objects.

These new modules were added to improve the handling and formatting of streams in the `odooghost` project. ([`c557159`](https://github.com/remyz17/odooghost/commit/c55715931ff269665f4142c7a37d5fc1df4fba35))

* feat(odooghost): add support for configuration file &#39;config.py&#39; to define stack configurations

feat(odooghost): add support for typing in services

fix(odooghost): fix typo in validate_version method name

fix(odooghost): fix typo in validate_version method name

fix(odooghost): fix typo in validate_name method name

feat(odooghost): add Stack class to manage stack configurations and services

feat(odooghost): implement ls method to list available stacks

feat(odooghost): implement init method to initialize a stack from a configuration file

feat(odooghost): implement _ensure_base_images method to ensure base images are available

feat(odooghost): implement _build_images method to build custom images ([`b034b10`](https://github.com/remyz17/odooghost/commit/b034b10cf1b5a764808b8f5bbcf4ff528cb396f1))

* feat(stack.py): add search class method to Stack class
feat(stack.py): add _ensure_base_images method to Stack class to ensure base images are present
feat(stack.py): add _build_images method to Stack class to build images ([`a3b6e47`](https://github.com/remyz17/odooghost/commit/a3b6e47b6e0217608c6d1903cc05a53248094f87))

* feat(renderer.py): add new module for rendering custom Dockerfile for Odoo image

feat(Dockerfile.j2): add template for rendering Dockerfile with Odoo version and optional dependencies

The new `renderer.py` module is added to handle the rendering of a custom Dockerfile for the Odoo image. It uses the Jinja2 template engine to render the Dockerfile based on the provided Odoo version and optional apt and pip dependencies.

The `Dockerfile.j2` template is also added, which includes the base image as `odoo:{{ odoo_version }}`. It also includes conditional blocks to install any specified apt or pip dependencies.

This change allows for more flexibility in customizing the Odoo image by providing a way to easily generate a Dockerfile with specific dependencies. ([`5d73497`](https://github.com/remyz17/odooghost/commit/5d734979081a2a3204479b46551a103002440ce9))

* feat(exceptions.py): add StackAlreadyExistsError class to handle the case when a stack already exists ([`53a076c`](https://github.com/remyz17/odooghost/commit/53a076c8468f334572334e5bd93ca6e95feec5e8))

* feat(root.py): add support for creating multiple stacks at once

The `create` command in `root.py` now accepts a list of stack configuration files as an argument. This allows users to create multiple stacks in one command.

Each stack configuration file is processed individually, and the `create` method of the `Stack` class is called for each file. This ensures that each stack is created separately.

This change improves the usability of the CLI tool by providing a convenient way to create multiple stacks with a single command. ([`6ced26c`](https://github.com/remyz17/odooghost/commit/6ced26c60c3d7f50254b0e9d30058abf953513bf))

* feat(exceptions.py): add new exception classes StackException, StackImageEnsureError, and StackImagePullError to handle specific errors related to stack operations ([`68661af`](https://github.com/remyz17/odooghost/commit/68661af8612e9b2bec07f4d5a3e05ac5f1fe7576))

* feat(stack.py): add validation for Odoo version in OdooStackConfig
add methods for listing and inspecting stacks
add methods for managing stack lifecycle (create, drop, update, start, stop, restart)
add properties for accessing stack name, Odoo service, and Postgres service
add property for checking if stack exists ([`d7fb32d`](https://github.com/remyz17/odooghost/commit/d7fb32d347f7f76e5b2776c35722a4da53f9ccd5))

* feat(services): add new services module with base, odoo, and postgres modules

The new services module is added to the odooghost package. It includes three modules: base, odoo, and postgres.

The base module contains the abstract base class `BaseService` which defines the common functionality for all services. It includes a method `ensure_image()` to ensure that the required Docker image is available. The `image_tag` property is defined as an abstract property.

The odoo module contains the `OdooService` class which extends `BaseService`. It takes a `config` parameter of type `stack.OdooStackConfig` and sets it as an instance variable. The `image_tag` property is implemented to return the image tag based on the version specified in the config.

The postgres module contains the `PostgresService` class which also extends `BaseService`. It takes a `config` parameter of type `stack.PostgresStackConfig` and sets it as an instance variable. It includes an `is_remote` property to check if the type of the config is &#34;remote&#34;. The `image_tag` property is implemented to return the image tag based on the version specified in the config. ([`5df2042`](https://github.com/remyz17/odooghost/commit/5df204217aad574651b794f1680510a97c4ae7a2))

* feat(cli): add stack subcommands to manage Odoo stacks

- Add `stack/__init__.py` to expose the `cli` object from `stack/root.py`
- Add `stack/root.py` to implement stack subcommands for managing Odoo stacks
- Add `check` command to validate stack configurations
- Add `create` command to create one or more stacks
- Add `drop` command to drop a stack and its related data
- Add `update` command to update a stack
- Add `start` command to start a stack
- Add `stop` command to stop a stack
- Add `restart` command to restart a stack
- Add `ls` command to list created stacks
- Add `ps` command to list running stacks ([`862fde4`](https://github.com/remyz17/odooghost/commit/862fde47667f5c64ccaa6e4a8a1bdce62362e2bd))

* feat(stack.py): add new file stack.py to implement a Stack class for managing stack configurations
feat(stack.py): add PostgresStackConfig class to represent the configuration for a Postgres stack
feat(stack.py): add DependenciesConfig class to represent the configuration for stack dependencies
feat(stack.py): add AddonsConfig class to represent the configuration for addons in a stack
feat(stack.py): add OdooStackConfig class to represent the configuration for an Odoo stack
feat(stack.py): add StackConfig class to represent the overall stack configuration
feat(stack.py): implement Stack class with constructor and from_file method for loading stack configurations from a file ([`6ba033b`](https://github.com/remyz17/odooghost/commit/6ba033be8774dd59e030042ee5338f7f57bbaed6))

* feat(cli): add support for &#39;version&#39; command to print OdooGhost version
fix(cli): improve error handling and logging in &#39;setup&#39; command
feat(cli): add support for &#39;drop&#39; command to drop OdooGhost environment and related data
feat(cli): add support for &#39;web&#39; command to run OdooGhost webserver
feat(cli): add &#39;stack&#39; subcommands to manage Odoo stacks ([`6aee7bf`](https://github.com/remyz17/odooghost/commit/6aee7bfb58837f903431432c10b080bd6d89f432))

* feat(config.py): add version and working_dir commands to the CLI for printing config version and working directory respectively
fix(config.py): remove NotImplementedError from version and working_dir commands as they are not yet implemented ([`32c14d5`](https://github.com/remyz17/odooghost/commit/32c14d53189625968a4ea4f2815e23ea6db0ea58))

* feat(logger.py): add InterceptHandler class to convert default logging LogRecord to loguru format
feat(logger.py): add setup_cli_logging function to configure logger for CLI
feat(pyproject.toml): add loguru dependency to enable loguru logging library in the project
fix(pyproject.toml): fix odooghost script entry point to point to the correct module and function ([`d4896e5`](https://github.com/remyz17/odooghost/commit/d4896e58e5274004c6eb0fd133a5d9b16343a73a))

* feat(cli): add &#39;setup&#39; command to initialize OdooGhost environment

- Added a new command &#39;setup&#39; to the CLI to initialize the OdooGhost environment.
- The &#39;setup&#39; command takes a required argument &#39;working_dir&#39; which specifies the directory where the OdooGhost environment will be set up.
- If the specified directory does not exist, it will be created.
- If the specified directory exists and is not empty, an error message will be displayed.
- The &#39;setup&#39; command creates the necessary directories for the OdooGhost environment: &#39;config.yml&#39;, &#39;data&#39;, and &#39;plugins&#39;.
- The &#39;config.yml&#39; file is created with the version and working directory information.
- If the OdooGhost environment is already set up, an error will be raised.

feat(context): add Context class to manage OdooGhost environment

- Added a new module &#39;context.py&#39; to manage the OdooGhost environment.
- The &#39;Context&#39; class is responsible for handling the setup state of the OdooGhost environment.
- The &#39;Context&#39; class has a &#39;check_setup_state&#39; method to check if the OdooGhost environment is already set up.
- The &#39;Context&#39; class has a &#39;setup&#39; method to set up the OdooGhost environment.
- The &#39;setup&#39; method creates the necessary directories and the &#39;config.yml&#39; file with version and working directory information.
- If the OdooGhost environment is already set up, an error will be raised.

feat(exceptions): add custom exceptions for OdooGhost

- Added a new module &#39;exceptions.py&#39; to define custom exceptions for OdooGhost.
- The &#39;OdooGhostException&#39; class is the base exception class for all OdooGhost exceptions.
- The &#39;ContextAlreadySetupError&#39; class is a specific exception that is raised when the OdooGhost environment is already set up. ([`f25e3e2`](https://github.com/remyz17/odooghost/commit/f25e3e27069d75f48506185c936f8ffe5b13c5db))

* feat: add OdooGhost entry point file

Add a new file `__main__.py` in the `odooghost` directory to serve as the entry point for the OdooGhost application.

feat: add main module for CLI

Add a new file `main.py` in the `odooghost/cli` directory to define the main module for the OdooGhost command-line interface (CLI).

chore: update project version

Update the version of the project in the `pyproject.toml` file from `0.1.0-alpha1` to `0.1.0`.

feat: add typer dependency

Add the `typer` dependency to the project in the `pyproject.toml` file with a version constraint of `^0.9.0`.

feat: add odooghost script

Add a script entry for `odooghost` in the `pyproject.toml` file to run the `odooghost.cli.main:cli` command as the entry point for the `odooghost` script. ([`10fd969`](https://github.com/remyz17/odooghost/commit/10fd9698bc7e986c2d610f4e7825d8a4441613b9))

### Fix

* fix(cli/stack/root.py): pass &#39;volumes&#39; argument to &#39;drop&#39; method in Stack class to enable dropping services volumes
fix(services/base.py): add &#39;raise_not_found&#39; parameter to &#39;get_container&#39; method in BaseService class to control whether to raise an exception when container is not found or not
fix(services/base.py): add warning message when trying to create a service container that already exists and force option is not used
fix(stack.py): pass &#39;force&#39; argument to &#39;create&#39; method in PostgresService and OdooService classes to enable recreating the containers ([`1ffeb84`](https://github.com/remyz17/odooghost/commit/1ffeb848496850c185aa60e799348daf4137e78f))

* fix(base.py): uncomment the line to remove the build context directory to prevent it from accumulating unnecessary files
fix(base.py): update the default image option to use the custom image tag if available, otherwise use the base image tag ([`1da8e0a`](https://github.com/remyz17/odooghost/commit/1da8e0a53852ce1b4c9a0089291893aa11bc38eb))

* fix(odoo.py): add null check for python dependencies before iterating over files to prevent potential error when no files are present ([`91f8981`](https://github.com/remyz17/odooghost/commit/91f8981d8e48090be05aa9713ea1b6f4d649a3f5))

* fix(config.py): improve name property to remove &#34;.git&#34; suffix from origin URL when type is not &#34;local&#34;
fix(config.py): update container_posix_path property to use mode variable instead of hardcoding &#34;copy&#34; ([`f4913c6`](https://github.com/remyz17/odooghost/commit/f4913c6f74bb9ffa3b5c01670937fb12c943c46a))

* fix(base.py): remove abstractmethod decorator from _prepare_build_context method
fix(odoo.py): call super()._prepare_build_context instead of super()._clean_build_context
fix(stack.py): change default value of ensure_addons parameter in create method to True ([`c55dcc5`](https://github.com/remyz17/odooghost/commit/c55dcc54ae2da55ab588a3a13049d3a51806aa95))

* fix(config.py): add field serializer for &#39;path&#39; attribute in AddonsConfig class to convert Path object to string representation
This was causing JSON serializer to throw exception because it does not know how to serialize pathlib.Path ([`96d8f1d`](https://github.com/remyz17/odooghost/commit/96d8f1d99afd661ae21dcd90478b184d1b161f72))

* fix(context.py): fix typo in variable name &#39;_stack_manager._working_dir&#39; to &#39;_stack_dir&#39; to correctly create the directory ([`09e91fe`](https://github.com/remyz17/odooghost/commit/09e91fe3ba8a3cc6302726b8cb14d34cea1aa189))

* fix(SettingsView.vue, StackView.vue, UsageView.vue): replace placeholder content with VErrorAlert component to indicate that the sections are not implemented yet ([`e8e5518`](https://github.com/remyz17/odooghost/commit/e8e5518aa01ea5ce338124c53a0ea19de31fff7b))

* fix(root.py): remove unnecessary raise NotImplementedError() and implement ps() function to list running stacks
fix(root.py): catch and log StackAlreadyExistsError exception when creating a stack ([`69b62e4`](https://github.com/remyz17/odooghost/commit/69b62e44f3a2042a622ddad4c04ed7a69461d70c))

* fix(cli/stack/root.py): add &#39;wait&#39; parameter to the &#39;stop&#39; function call in the &#39;stop&#39; command to allow waiting for containers to stop
fix(stack.py): add &#39;wait&#39; parameter to the &#39;stop&#39; function to allow waiting for containers to stop ([`98e08df`](https://github.com/remyz17/odooghost/commit/98e08df88eedea225c17830b017d59a6987ddc83))

* fix(root.py): change stack_configs argument to stack_names to follow last Context changes
feat(root.py): implement ls command to list created stacks ([`876bc1a`](https://github.com/remyz17/odooghost/commit/876bc1aa17072c4ad73905210e9401b1471af296))

* fix(odoo.py, postgres.py): change method call from _get_container_labels() to labels() to follow recent BaseService changes ([`1ab0339`](https://github.com/remyz17/odooghost/commit/1ab0339a6e47b33cb06607fe070282ac01c4875d))

* fix(context.py): add error handling for non-existent stack config file in get method
feat(context.py): add drop method to remove stack from context ([`ae62974`](https://github.com/remyz17/odooghost/commit/ae62974541a698ab5d9adbda592068a45d8d0b5c))

* fix(config.py): add type hinting to string_to_list method in DependenciesConfig class to improve code readability and maintainability
fix(config.py): fix typo in validate_version method in OdooStackConfig class
fix(config.py): add type hinting to validate_name method in StackConfig class to improve code readability and maintainability ([`6c7c813`](https://github.com/remyz17/odooghost/commit/6c7c813be446c69454975fadd7aa120f5558d1e8))

* fix(stack.py): import correct function labels_as_list from odooghost.utils.misc instead of odooghost.utils.docker
feat(stack.py): add docstrings to StackState enum and its members to improve code documentation
feat(stack.py): add docstrings to Stack class methods and properties to improve code documentation
feat(stack.py): add __repr__ and __eq__ methods to Stack class for better representation and comparison of Stack instances ([`b0ef375`](https://github.com/remyz17/odooghost/commit/b0ef375f4f0b5d3635815932992fffddcd0b57e6))

* fix(container.py): fix passing options argument to _create_container_args function

The options argument was not being passed correctly to the _create_container_args function. This commit fixes the issue by removing the double asterisks before the options argument. ([`a8c0ed8`](https://github.com/remyz17/odooghost/commit/a8c0ed808e90f707e89e15d1bc9957f10042c352))

* fix(stack.py): add check for stack existence before starting, stopping, or restarting to prevent errors when stack does not exist
feat(stack.py): add logging messages for stopping and restarting containers to provide better feedback to the user
feat(stack.py): add check for no containers to stop or restart and log a warning message to inform the user ([`32fe8ad`](https://github.com/remyz17/odooghost/commit/32fe8ad022cb265b008d23b9bfd41ef70f5f3cb4))

* fix: CI was fixed ([`bc87841`](https://github.com/remyz17/odooghost/commit/bc87841fcc0aa700b655d28140693191bbc0328c))

* fix(exceptions.py): add StackNotFoundError class to handle cases when a stack is not found
fix(stack.py): add check for stack existence before dropping it to prevent errors when trying to drop a non-existent stack
feat(stack.py): use Docker API to check if a stack exists instead of listing containers to improve performance ([`d7bd98b`](https://github.com/remyz17/odooghost/commit/d7bd98b85573f775ac660d91deabcf3fdd591300))

* fix(base.py): handle APIError when creating volumes in BaseService.create_volumes() method to provide more informative error message
refactor(postgres.py): delegate volume creation to the parent class in PostgresService.create_volumes() method to avoid code duplication ([`d2e46ba`](https://github.com/remyz17/odooghost/commit/d2e46baf9b9bcc5668a603b3f3f0ad3a8262dae8))

* fix(odoo.py): change the signature of the build_image method to accept optional parameters rm and no_cache
fix(odoo.py): add logic to retrieve the image ID after building the Odoo custom image
feat(progress_stream.py): add function get_image_id_from_build to extract the image ID from the build events list ([`8f6cedd`](https://github.com/remyz17/odooghost/commit/8f6cedd8279c6f52b0a49cf853cb75ad62be4902))

* fix(cli/stack/root.py): catch additional exceptions when creating stack from config file to improve error handling
feat(stack.py): add support for ensuring addons during stack creation to provide flexibility ([`eac0737`](https://github.com/remyz17/odooghost/commit/eac0737fb1749781b9bc672401d4d0f54e90f849))

* fix(odoo.py): add missing import statements for sys, BytesIO, logger, exceptions, renderer, utils, and ctx
feat(odoo.py): add support for building custom Odoo image with specified dependencies
feat(odoo.py): add property to generate base image tag based on Odoo version
feat(odoo.py): add property to generate image tag for custom Odoo image based on stack name and Odoo version
feat(odoo.py): add property to check if custom image is available for Odoo service ([`5756990`](https://github.com/remyz17/odooghost/commit/575699037d35d94b7d45c66322a24ce162d63eaa))

* fix(postgres.py): add stack_name parameter to PostgresService constructor to improve clarity and usage
feat(postgres.py): add ensure_base_image method to PostgresService to handle remote type configuration
fix(postgres.py): rename image_tag property to base_image_tag for clarity and consistency ([`4f424cf`](https://github.com/remyz17/odooghost/commit/4f424cf89b536d428bbe513efa598326d798cedc))

* fix(exceptions.py): fix syntax error ([`86230f9`](https://github.com/remyz17/odooghost/commit/86230f9054b5042ace5d7c751feae961f16ba787))

* fix(base.py): change import statement from ImageNotFound to NotFound to match the actual import
feat(base.py): add support for pulling the base image if it is not found
feat(base.py): add abstract method build_image() to be implemented by subclasses
feat(odoo.py): implement build_image() method to build custom image for Odoo service
feat(odoo.py): implement has_custom_image property to indicate that Odoo service has a custom image
feat(postgres.py): implement build_image() method to build custom image for Postgres service
feat(postgres.py): implement has_custom_image property to indicate that Postgres service does not have a custom image ([`2a9cdff`](https://github.com/remyz17/odooghost/commit/2a9cdffd163dec8a0caa46465817833e06ee3961))

* fix(__main__.py): call main function directly instead of main.cli() to fix import error
feat(__main__.py): add logger setup before calling main function to enable logging in the CLI
feat(cli/__init__.py): create main function to set up CLI logging and call cli() function
feat(cli/config.py): add config subcommands to manage OdooGhost config
feat(cli/root.py): add setup command to set up OdooGhost environment ([`7793c0a`](https://github.com/remyz17/odooghost/commit/7793c0a7f6c6887256fd429bceebab269def7df8))

### Refactor

* refactor(base.py): remove unnecessary code block for handling NotFound exception in BaseService class ([`991fad2`](https://github.com/remyz17/odooghost/commit/991fad2074b2cd313d33ad8539d748a37c54f88a))

* refactor(config.py): rename &#39;postgres&#39; attribute to &#39;db&#39; in StackServicesConfig class for better clarity and semantics
refactor(base.py): update &#39;config&#39; property in BaseService class to access the &#39;services&#39; attribute in stack_config for improved readability and consistency ([`bd2dd85`](https://github.com/remyz17/odooghost/commit/bd2dd851204b151665272b65b28d8d96ea62fa35))

* refactor(stack): Stack services are now under services config option ([`8704973`](https://github.com/remyz17/odooghost/commit/8704973689110042572be14398493359dd62396b))

* refactor(root.py): replace specific exception handling with a generic StackException to improve code readability and maintainability ([`aaa53c6`](https://github.com/remyz17/odooghost/commit/aaa53c69084612d86f674401d4b1c95097644d7a))

* refactor(addons.py): rename _addons_config to config for better readability ([`f48ddf3`](https://github.com/remyz17/odooghost/commit/f48ddf3876e47bc42514f9ac86c46adbe8778311))

* refactor(odoo.py): extract _get_mounts method to improve readability and maintainability ([`fd1fac1`](https://github.com/remyz17/odooghost/commit/fd1fac12e570604ee1972a3660f8c0052b536ecc))

* refactor(addons.py): extract common logic into a private method `_get_addons` to improve code readability and maintainability
feat(addons.py): add `get_mount_addons` method to retrieve addons with mode &#34;mount&#34;
fix(addons.py): update `get_addons_path` method to use `_get_addons` instead of `get_copy_addons` to include addons with both &#34;copy&#34; and &#34;mount&#34; modes ([`d3cae2a`](https://github.com/remyz17/odooghost/commit/d3cae2ae19eecb74cc5d8e2d65c08a879852464e))

* refactor: Move AddonsCopy in addons config directly ([`a93cf09`](https://github.com/remyz17/odooghost/commit/a93cf097e72539ced41d71bb58d5190a99e461fc))

* refactor(odoo.py): simplify logic for copying addons and requirements files
feat(odoo.py): add support for custom command line arguments to be passed to the Odoo container ([`37b5063`](https://github.com/remyz17/odooghost/commit/37b50633e6c9ffb7a7566ceff7452838e0f76240))

* refactor(base.py): refactor build_context method to use try-finally block for better exception handling and resource cleanup ([`79340f7`](https://github.com/remyz17/odooghost/commit/79340f722284ea6d320cc2f062305b9b31a902aa))

* refactor(config.py): add serialization logic for &#39;files&#39; field in PythonDependenciesConfig class to convert Path objects to string paths
feat(config.py): add utility methods in PythonDependenciesConfig class to get mount path, file hash, and file mount path for pip requirements ([`6c830d6`](https://github.com/remyz17/odooghost/commit/6c830d6fc5f20a8dd7f5967fca9b3771982d1bea))

* refactor(addons.py): replace hashlib.md5 with get_hash function for generating name_hash
refactor(addons.py): add get_addons_path method to return a comma-separated string of container_posix_path
refactor(addons.py): add has_copy_addons and has_mount_addons properties to check if there are addons with mode &#34;copy&#34; or &#34;mount&#34;
fix(addons.py): fix typo in InvalidAddonsPathError message ([`200bde7`](https://github.com/remyz17/odooghost/commit/200bde7b4aa96202b3be4ce1b1f7e6a3498e2332))

* refactor(exceptions.py): move CommonNetworkEnsureError to StackException for consistency and clarity ([`39b446d`](https://github.com/remyz17/odooghost/commit/39b446d436f2f8dc532505c592abff0596c0b914))

* refactor(container.py): simplify get_subnet_ip method to return the first IP address from networks dictionary

The `get_subnet_ip` method in the `Container` class was simplified to return the first IP address from the `networks` dictionary. The previous implementation used a loop to collect all IP addresses and returned the first one if there was only one IP address, otherwise it returned a list of IP addresses. The new implementation directly returns the value of the first IP address from the dictionary. This simplifies the code and improves readability. ([`9a177a6`](https://github.com/remyz17/odooghost/commit/9a177a6d513d5b9decd051ed9b8cfa3e8206c699))

* refactor(odoo.py): extract labels into a separate method for better code organization and readability ([`fdfc060`](https://github.com/remyz17/odooghost/commit/fdfc06027ce6a6c430b07d9e41e7565d31889062))

* refactor(stack.py): move logger.info statements to appropriate locations for better readability and consistency
feat(stack.py): add saving and dropping of stack config to ensure proper management of stack configurations ([`4ac0a3a`](https://github.com/remyz17/odooghost/commit/4ac0a3af1d09051de243be3795d89a1c6a08e364))

* refactor(base.py): change return type of labels() method from dict[str, str] to Labels class for better type safety and readability ([`4cda872`](https://github.com/remyz17/odooghost/commit/4cda872c6f3b72c3d6b3e5fe472bebc9f35f323f))

* refactor(base.py): update import statement for labels_as_list function to reflect new module structure

The import statement for the `labels_as_list` function in the `odooghost.utils.docker` module has been updated to `odooghost.utils.misc` module. This change was made to reflect the new module structure and improve code organization. ([`7ff44ef`](https://github.com/remyz17/odooghost/commit/7ff44ef94affce07f8db7a106253633e13eb6d9b))

* refactor(container.py): change get_container_name method to use type hints and improve variable names for better readability
refactor(container.py): add type hints to the __init__ method of the Container class
refactor(container.py): add type hints to the get_value method of the Container class
refactor(container.py): add type hints to the start, stop, kill, restart, and remove methods of the Container class
feat(container.py): add stream_logs method to stream logs to a specified stream
refactor(container.py): add type hints to the stream_logs method
refactor(container.py): add type hints to the stack and service properties of the Container class
refactor(container.py): add type hints to the __repr__ method of the Container class
refactor(container.py): add type hints to the __eq__ method of the Container class ([`abee633`](https://github.com/remyz17/odooghost/commit/abee63387a4d135ab04cbafb9f91a05f493eab6d))

* refactor(utils): rename docker module to misc module for better clarity and consistency ([`f7a286c`](https://github.com/remyz17/odooghost/commit/f7a286c4eafd03483d56fa8f8b8b2cd7cc70dd06))

* refactor(base.py): rename _get_container_labels() method to labels() for better clarity and consistency
refactor(base.py): use self.labels() method instead of _get_container_labels() method to retrieve container labels
refactor(base.py): use self.labels() method instead of _get_container_labels() method to filter containers by labels ([`1ccc494`](https://github.com/remyz17/odooghost/commit/1ccc494bea1ea8707785c8fda5f234665955911a))

* refactor(root.py): import Stack class directly from odooghost.stack module for better readability and maintainability
fix(root.py): fix incorrect method calls to Stack class by removing unnecessary &#39;stack.&#39; prefix ([`a4848d6`](https://github.com/remyz17/odooghost/commit/a4848d6456f13470d430a107bc6389dddafa244f))

* refactor(context.py): add support for managing stack configurations in a separate directory
feat(context.py): add method to get the path of a stack configuration file based on stack name ([`f52c81b`](https://github.com/remyz17/odooghost/commit/f52c81bd6b7242ee2b2a407824ce4ea0048a6098))

* refactor(odoo.py, postgres.py): remove unused imports and methods, simplify create_container method ([`91fe402`](https://github.com/remyz17/odooghost/commit/91fe402f35e6c070337e6a617687acee5133ab17))

* refactor(base.py): remove abstractmethod decorator from some methods
feat(base.py): add create_container method to create a new container with given options
feat(base.py): add start_container method to start the container associated with the service
feat(base.py): add get_container method to retrieve the container associated with the service ([`b7449a8`](https://github.com/remyz17/odooghost/commit/b7449a8f3cf336fff14ea0ca645b9802ed5a0a22))

* refactor(utils): move docker related functions to separate module for better organization and maintainability
feat(utils/docker.py): add `labels_as_list` function to convert dictionary of labels to a list of strings ([`c722923`](https://github.com/remyz17/odooghost/commit/c7229233c116f7da01a4f412eb0075e09f72309c))

* refactor(logger.py): add return type annotation to the emit method in InterceptHandler class for better code readability and maintainability ([`e57c95f`](https://github.com/remyz17/odooghost/commit/e57c95f46f0a2a3f60f01d243af917f24279b667))

* refactor(odoo.py): move &#39;_get_container_labels&#39; method to the base class &#39;BaseService&#39; for code reuse
fix(odoo.py): update &#39;create_container&#39; method to handle APIError and raise a custom exception if container creation fails ([`2f929d8`](https://github.com/remyz17/odooghost/commit/2f929d8c1f48aeb4e8a5a2205b84a5a3661ae913))

* refactor(stack.py): remove unused methods _ensure_base_images and _build_images to simplify code and improve readability
feat(stack.py): add creation of common network before creating services to ensure proper communication between services ([`1259077`](https://github.com/remyz17/odooghost/commit/125907762370bbdad20422cf4c40f058ef6307f1))

* refactor(postgres.py): Follow last BaseService changes

feat(postgres.py):
- Add support for creating volumes for the db container
- Add support for creating the db container with the necessary environment variables and mounts ([`9c32f32`](https://github.com/remyz17/odooghost/commit/9c32f32cf85490abb4652232b9835570368814c9))

* refactor(odoo.py): follow last BaseService changes ([`78d9ed6`](https://github.com/remyz17/odooghost/commit/78d9ed6ff60d8ca6679ab991ce2dfaa1ab939e17))

* refactor(context.py): change return type annotation of docker method from docker.Client to &#34;docker.DockerClient&#34; for better type hinting and clarity ([`65c51e5`](https://github.com/remyz17/odooghost/commit/65c51e5b176e0cdf281939b538029f7c3a43871f))

* refactor(context.py): add docker client property to Context class for better code organization and reusability
feat(context.py): add docker import statement to support docker client usage in Context class ([`135d0ae`](https://github.com/remyz17/odooghost/commit/135d0ae67f09cde4d089b71aa8df13f15a1f4c8f))

* refactor(context.py): remove unused variable and unnecessary TODO comment ([`213053e`](https://github.com/remyz17/odooghost/commit/213053e1d66d1fe448cda5c21e3f9df664c27e6a))

### Unknown

* doc(config.py): add comprehensive comments to improve code readability and documentationn ([`0d0fafe`](https://github.com/remyz17/odooghost/commit/0d0fafe5f01b181dfe2191814d7db24c14ac3dc9))

* Merge pull request #1 from remyz17/stack+configs

feat: implement Stack config managment in context ([`be16cd4`](https://github.com/remyz17/odooghost/commit/be16cd4c5b16ebb139a823ccf4602dd140814dc5))

* doc(context.py): improve code readability and add docstrings to methods and classes ([`d8a325d`](https://github.com/remyz17/odooghost/commit/d8a325d9e8f40ba0339970a1667852e030d1220b))

* Initial commit ([`235a6c5`](https://github.com/remyz17/odooghost/commit/235a6c572a0f2d2934d7d7699448e60f545fe7f0))