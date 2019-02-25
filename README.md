# gabe565/0bin

An alpine-based docker image to run [0bin](https://github.com/sametmax/0bin).

# Quick Start

Run the 0bin image:

```sh
docker run --name 0bin --detach gabe565/0bin
```

If you wil access the image from another machine, you will need to add the server port mapping. This example will bind to port 8080 of the host machine:

```sh
docker run --name 0bin -p 8080:80 -d gabe565/0bin
```

For data persistance, make sure that the `/data` directory is bound to a volume or local directory.

```sh
docker volume create 0bin_data
docker run --name 0bin -p 8080:80 -v 0bin_data:/data -d gabe565/0bin
```

# Environment

Most of the [original 0bin options](https://0bin.readthedocs.io/en/latest/en/options.html) can be changed through environment variables to allow for customization.     
Some of the defaults have been changed to work more smoothly with Docker, listed below.

| Variable                | Description                                                                                                                                                        | Default Value                                                                                                             |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| HOST                    | IP address to bind to.                                                                                                                                             | `0.0.0.0`                                                                                                                 |
| PORT                    | Post to listen on.                                                                                                                                                 | `80`                                                                                                                      |
| DEBUG                   | Enable debug output on 500 errors and watch files for hotswapping.                                                                                                 | `false`                                                                                                                   |
| USER                    | The user to run under after startup.                                                                                                                               | `root`                                                                                                                    |
| GROUP                   | Group to run under after startup.                                                                                                                                  | Match `USER`                                                                                                              |
| COMPRESSED_STATIC_FILES | Serve minified css and js files.                                                                                                                                   | `true`                                                                                                                    |
| PASTE_FILES_ROOT        | Location to store encrypted paste files.                                                                                                                           | `/data`                                                                                                                   |
| CUSTOM_TEMPLATE_DIR     | Location of custom template files. Templates here take precedence over the built-in templates.                                                                     | `/views`                                                                                                                  |
| MENU                    | Allows the navigation menu to be changed.                                                                                                                          | `[["Home","/"],["Download 0bin","https://github.com/sametmax/0bin"],["Faq","/faq/"],["Contact","mailto:your@email.com"]]` |
| MAX_SIZE                | Maximum paste filesize. Careful with this one since pastes are client-side encrypted. Large files can slow down a user's browser.                                  | ~500KB                                                                                                                    |
| DISPLAY_COUNTER         | Enable or disable the paste counter in the page footer.                                                                                                            | `true`                                                                                                                    |
| REFRESH_COUNTER         | How often to refresh the paste counter.                                                                                                                            | `60 * 1`                                                                                                                  |
| PASTE_ID_LENGTH         | Length of the generated URL paste ID.                                                                                                                              | `8`                                                                                                                       |
| BURN_ACTIVATION_SECONDS | Burn after reading waits this number of seconds before actually burning when read.                                                                                 | `10`                                                                                                                      |
| KEEP_ALIVE_USER_AGENTS  | Burn after reading will not burn if the requesting user agent is in this list. WARNING: This one could cause security issues and is not recommended in most cases. | `[]`                                                                                     |

# Theming

The **CUSTOM_TEMPLATE_DIR** environment variable allows for a directory to be used for modified templates while still falling back to the defaults. This location defaults to `/views`.

## Pulling the Default Templates

To pull these into a local directory, run the following with the container running:

```sh
docker cp 0bin:/app/zerobin/views views 
```

Then the templates will be available for modification in your local directory.

## Serving Custom Templates

To serve these templates in the container, restart it with a read-only volume binding to `./views`:

```sh
docker run --name 0bin -p 8080:80 -v data:/data -v ./views:/views:ro -d gabe565/0bin
```
