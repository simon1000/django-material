0.12.0 2017-01-24 - Beta
------------------------
* Forms - Fix select rendering
* Forms - Fix date and datetime fields rendering
* Frontend - Refactor datatables list view
* Frontend - Fix viewset incompatibility under python 2.7
* Frontend - Natural default theme color
* Frontend - Prebuild theme set
* Frontend - Custom theme builder management command (PRO)
* Frontend - Generic views templates now extends base module template
* Frontend - Improve base 2 columns layout
* Admin - Add "Save as New" change form action
* Admin - Fix redirect after login

0.11.0 2016-12-13 - Beta
------------------------

* Forms - Default theme secondary color changed to green
* Frontend - Added `startmodule` management command
* Frontend - Added list view actions (PRO)
* Frontend - Integration with django-filters (PRO)
* Frontend - Active page highlight fixed under IE/Safari
* Admin - Fix ManyToMany field height
* Admin - Fix change form markup

0.10.1 2016-11-10 - Beta
------------------------

- Fix admin raw_id select on django 1.10


0.10.0 2016-10-31 - Beta
------------------------

- Forms - Upgrade to Materialize CSS 0.97.8
- Frontend, Admin - New sidebar with user photo
- Frontend, Admin - Massive CSS/JS/HTML cleanup
- Frontend, Admin - Serve minfied js/css in the production mode
- Frontend - Switch from unsupported PJAX to Turbolinks!
- Admin - Use `model_admin.has_module_permission()` permission check

0.9.2 2016-10-27 - Beta
-----------------------

- Fix admin read-only field for simple values


0.9.1 2016-10-18 - Beta
-----------------------

- Fix duplicate error message for admin non field error.


0.9.0 2016-10-17 - Beta
-----------------------

- Forms - Add Formset and Inlines Form fields (PRO)
- Forms - Add input[type=range] support
- Forms - Fix initial label position for datetime field with value
- Forms - Fix initial label position for number field with zero as initial value
- Forms - Fix XSS vulnerability in input fields.
- Forms - Fix CSS inclusion default template
- Frontend - Fix module delete
- Frontend - Add CRUD views and viewset
- Frontend - Remove LOGIN_REDIRECT_URL override on frontend autoregister
- Admin - User `user.get_username` instead of `user.username`
- Admin - Django 1.9/1.10 compatibility
- Admin - Readonly field support in inlines
- Admin - Use `AdminSite.site_url` as back link

0.8.0 2016-06-14 - Beta
-----------------------

First beta release.

* Forms - Fix 0 as initial value for number input
* Forms - Remove Roboto font fix hack on windows
* Frontend - module heareds fixed
* Admin - list sorting support
* Admin - fixedHeader fixed
* Admin - fix pagination display bug under dj19
* Admin - lost actions support
* Admin - added datetime today shortcut links
* Admin - added filter for select multiple field
* Admin - readonly fields support for inlines
* Admin - mansory layout for index page
* Admin - added app and model icons support

0.7.0 2016-03-13 - Alpha
------------------------

The last alpha release.

* Forms - Fix controls in new forms in formsets
* Forms - New way to append or override widget attrs in template
* Forms - Removed `group_class`, `add_group_class`, `add_label_class` redefinable parts
* Admin - Match table styles to google guidelines.
* Admin - Start to work on admin widget support improvements http://forms.viewflow.io/demo/widget/admin/
* Admin - Fix scrollbar
* Frontend - Switch from fontawesome to material-design-iconic font
* Frontend - Fix broken links on user navigation menu
* Frontend - Modules are refactored to AppConfig mixins

0.6.0 2015-11-19 - Alpha
------------------------

* First release with full django standard widgets support
* Forms - New per-widget demos on http://forms.viewflow.io/demo/widget/
* Forms - Many widget behaviour fixes (DecimalInput, Select, MultiSelect, RadioInput)
* Forms - Disable change datetime on mouse wheel
* Admin - Style fixes and improvements
* Admin - Custom form layouts support (ex: http://forms.viewflow.io/admin/sales/shipment/add/)
* Admin - Admin css/js files modded to separate templates. Fix static files issue with CDN
* Admin - Move All js/css dependencies inside the package. Make it intranet app friendly.
* Frontend - Style fixes and improvements
* Frontend - Fix load indicator on pjax back

0.5.0 2015-11-19 - Alpha
------------------------

* Django 1.9 support
* Forms - Add latest materializecss
* Admin - Support for Readonly widget
* Admin - Custom admin site support
* Admin - Proper lang_code for html
* Admin - Tabular inlines formset support
* Admin - Fk and Many2Many fields support
* Frontend - Integrate django-easy-pjax into the app
* Frontend - Cancel animation as soon as page loaded


0.4.0 2015-05-29 - Alpha
------------------------

* Forms - CheckboxSelectMultiple widgets with multi-column layout support
* Forms - TimeInput widget support (thnks @Morozzzko)
* Forms - Dynamic formsets support 
* Admin - fix user change password form
* Frontend - support for smooth navigation back to initial page


0.3.0 2015-05-11 - Alpha
------------------------

* Migrated to new version of materializecss framework
* List all applications in admin navigation menu
* Added breadcrumbs in admin
* Custom material css and js cleanup
* New Frontend template
* Various widget rendering fixes (splitdatetime, empty selects)

0.2.1 2015-04-20 - Alpha
------------------------

* Fixed SplitDateTime widget rendering with empty value
* More consistent parts/variables names over widgets templates
* Fixed file field submission and validation
* Compact html output
* Added ellipses on long labels overflow


0.2.0 2015-04-03 - Alpha
------------------------
* Switched to material design
* Initial admin interface support


0.1.0 2014-11-05 - Alpha
------------------------

* First alpha version extracted from `Viewflow <http://viewflow.io>`_ library
* Basic django widgets support
