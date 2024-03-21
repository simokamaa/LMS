### Theme API
Use Template API class written in Python to efficiently use Vuexy templates in Django projects of any complexity.

### Template Helpers#
init_context() - Init the Template Context using TEMPLATE_CONFIG.
The init_context function is used to set up the initial context for a web application. It ensures that the application starts with predefined default settings, making it easier to maintain and customize.

### Use
 - The following configuration settings are assigned to their respective keys in the context dictionary:

"layout": Controls the layout of the application.
"theme": Specifies the visual theme or appearance of the application.
"style": Defines the overall style of the application.
"rtl_support": Indicates whether right-to-left (RTL) language support is enabled.
"rtl_mode": Specifies the RTL mode if enabled.
"has_customizer": Determines if the application has a customizer feature.
"display_customizer": Controls the visibility of the customizer.
"content_layout": Defines the layout of the content within the application.
"navbar_type": Specifies the type or style of the navigation bar.
"header_type": Specifies the type or style of the header.
"menu_fixed": Determines whether the menu is fixed in place.
"menu_collapsed": Specifies if the menu is initially collapsed.
"footer_fixed": Controls whether the footer is fixed in place.
"show_dropdown_onhover": Controls the behavior of dropdown menus (e.g., whether they appear on hover).
                  
### map_context() - Map context variables to template class, value, or variable names..
The map_context function is designed to facilitate the mapping of configuration variables to specific class names, values, or variables that are used in the frontend of a web application. This mapping is essential for controlling the visual appearance and behavior of the application based on various configuration settings.

get_theme_variables() - Get theme variables by scope.
The get_theme_variables function is responsible for retrieving theme-related variables or settings based on a specified scope.

get_theme_config() - Get theme config by scope.
The get_theme_config function provides an easy way to access and apply theme-related configuration settings based on a specified scope.

set_layout(view, context={})() - Set the current page layout and init the layout bootstrap file.
The set_layout function is responsible for configuring the layout of a web view or page within a web application. It determines which layout template should be used based on the view's filename and initializes the appropriate layout configuration.

Use
class HorizontalView(TemplateView):
### Predefined function
    def get_context_data(self, **kwargs):
#### A function to init the global layout. It is defined in web_project/__init__.py file
    context = TemplateLayout.init(self, super().get_context_data(**kwargs))

### Update the context
    context.update(
      {
        "layout": "horizontal",
        "layout_path": TemplateHelper.set_layout("layout_horizontal.html", context),
      }
    )

    TemplateHelper.map_context(context)

    return context
### Template Tags#
get_theme_variables(scope) this tag calls the get_theme_variables() helper to get the scope.
Use
{% get_theme_variables "THEME_VARIABLES" %}
get_theme_config(scope) this tag calls the get_theme_config() helper to get the scope.
Use
{% get_theme_config "TEMPLATE_CONFIG" %}
filter_by_url(submenu, url)
The filter_by_url filter is a useful tool for dynamically highlighting or marking active menu items in a navigation menu based on the current URL in a Django web application.

current_url(request)
The current_url function is utilized within the href attribute to retain the current page when switching between languages. This ensures a seamless transition without redirecting to a different page upon language change.

<!-- Language -->
<li class="nav-item dropdown-language dropdown me-2 me-xl-0">
    <a class="nav-link dropdown-toggle hide-arrow" href="javascript:void(0);" data-bs-toggle="dropdown">
    <i class='ti ti-language rounded-circle ti-md'></i>
    </a>
    <ul class="dropdown-menu dropdown-menu-end">
        ...
        <li>
          <a class="dropdown-item {% if LANGUAGE_CODE == 'de' %}active{% endif %}" href="{% current_url request %}" data-language="de" data-text-direction="ltr">
            <span class="align-middle">{% trans "German"%}</span>
          </a>
        </li>
        ...
    </ul>
</li>
<!--/ Language -->
