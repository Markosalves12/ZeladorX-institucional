# Architecture decisions

- Keep the public institutional UI independent from AdminLTE, using `templates/partials/_site_nav.html` and `setup/static/institutional/` so the corporate presentation can evolve without coupling to admin dashboard styles.
- Keep the existing public URL names and the `generic_view` content contract because published links and all current feature views depend on them.
- Initialize the institutional color theme in the document head and persist its selector under `zeladorx.institutional.theme` to avoid a flash of the wrong theme.
- Build immersive institutional motion with progressive-enhancement CSS 3D and pointer/scroll effects, always preserving reduced-motion and mobile fallbacks because investor presentation must remain accessible and fast.
