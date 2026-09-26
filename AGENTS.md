# Architecture decisions

- Keep the public institutional UI independent from AdminLTE, using `templates/partials/_site_nav.html` and `setup/static/institutional/` so the corporate presentation can evolve without coupling to admin dashboard styles.
- Keep the existing public URL names and the `generic_view` content contract because published links and all current feature views depend on them.