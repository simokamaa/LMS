📦
├── 📂 apps                             > Django app modules, which are individual components or features of your Django project.
├── 📂 config                           > Contains django project configuration.
│   ├── 📄 asgi.py                        > ASGI server configuration.
│   ├── 📄 context_processors.py          > Custom context processors for templates.
│   ├── 📄 settings.py                    > Django project settings.
│   ├── 📄 template.py                    > Template-related configuration (Personalize/Customize the project).
│   ├── 📄 urls.py                        > URL routing configuration.
│   └── 📄 wsgi.py                        > WSGI server configuration.
├── 📂 locale                           > Directory for localization files, including translations and internationalization resources.
├── 📂 nginx                            > Configuration files for the Nginx web server, used as a reverse proxy in front of Django applications.
├── 📂 src                              > Front-end assets source
│   ├── 📂 assets                         > Contain template static & generated assets
│   ├── 📂 fonts                          > Template Font-icons
│   ├── 📂 js                             > Core JS(ES6) files
│   ├── 📂 libs                           > Third-party libs i.e datatable, full-calender etc...
│   ├── 📂 scss                           > Core SCSS
│   ├── 📂 tasks                          > Gulp tasks
│   ├── 📄 build-config.js                > Build config file for asset generation
│   ├── 📄 gulpfile.js                    > Gulpfile
│   ├── 📄 package.json                   > Containing essential details like project metadata, dependencies, and scripts for tasks such as building, testing, and starting servers.
│   └── 📄 webpack.config.js              > Webpack file to transpile & bundle JS files.
├── 📂 templates                          > Django template files organized into subdirectories, typically including layouts and partials for rendering HTML.
│   ├── 📂 layouts
│   └── 📂 partials
├── 📂 web_project                      > Project-specific code and utilities.
│   ├── 📂 template_helpers                > Django template helpers.
│   └── 📂 template_tags                   > Django template tags.
├── 📄 .editorconfig                    > Configuration file for code editors to maintain consistent coding styles and formatting.
├── 📄 .env                             > Environment variables configuration file.
├── 📄 .env.prod                        > Environment variables specific to the production environment.
├── 📄 .gitattributes                   > Git attributes file for specifying how Git should handle files.
├── 📄 .gitignore                       > Git ignore rules to exclude files and directories from version control.
├── 📄 .dockerignore                    > Docker-specific rules for excluding files and directories when building Docker images.
├── 📄 .prettierignore                  > Rules for Prettier code formatter to ignore specific files and directories.
├── 📄 .prettierrc.json                 > Configuration file for Prettier.
├── 📄 db.sqlite3                       > The default SQLite database used during development.
├── 📄 docker-compose.yml               > Docker Compose configuration file for managing containers and services.
├── 📄 Dockerfile                       > Docker image configuration.
├── 📄 manage.py                        > Django's command-line tool for managing various aspects of the project.
└── 📄 requirements.txt                 > A list of Python dependencies required for your Django project.