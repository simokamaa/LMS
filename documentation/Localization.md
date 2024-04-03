## Django Localization

Django's localization features provide a convenient way to retrieve strings in various languages, allowing you to easily support multiple languages within your application.

## Built in localization for The Learning Management System

To provide a convenient way to retrieve strings in various languages, allowing you to easily support multiple languages within your application.

Language strings are stored in files within the /lang directory. Within this directory there should be a subdirectory for each language supported by the application:

Or, translation strings may be defined within PO files that are placed within the /locale directory. When taking this approach, each language supported by your application would have a corresponding PO file within this directory. This approach is recommended for application's that have a large number of translatable strings:

### Info:

You can modify the default language in this system by editing the LANGUAGE_CODE in the settings.py file. Be sure to clear your cookies after making this change to ensure that the new default language is applied.
A user's language preference can be stored in a cookie, and the name of this cookie is determined by the setting LANGUAGE_COOKIE_NAME, with the default name being django_language. refer How Django discovers language preference?

Heds up!: Updating LANGUAGE_CODE from settings.py file will not change the text text-direction (LTR or RTL) of the template. If you are using RTL language then you have to change the text-direction manually from scripts_includes.html file. Please to update rtl_mode value (True for RTL, False for LTR) from template.py
Use
📂 locale
├── 📂 en
│ └──📂 LC_MESSAGES
│ └──📄 django.po
└── 📂 fr
└──📂 LC_MESSAGES
└──📄 django.po


## How to add a New Language?#
To add support for a new language in your Django project:

Heads Up! : Ensure that there is a "locale" folder located at the root of your project.
Open your project's settings.py file.
Locate the LANGUAGES setting and add the desired language and locale code. For example:
Use
# Enable i18n and set the list of supported languages
LANGUAGES = [
  ("en", _("English")),
  ("fr", _("French")),
  ("ar", _("Arabic")),
  ("de", _("German")),
  # Add more languages as needed
]
en is the language code.
_("English") is the human-readable language name.
In your terminal, run the following command to generate the initial translation files (.po files) for your project:
Replace <locale_code> with the code for the new language (e.g., de for German).

### Use
python manage.py makemessages -l <locale_code>
Info: msgid will be generated only from Django apps html files where we have used translate for ex: {% translate "Academy" %}
In the locale/<locale_code>/LC_MESSAGES/ directory, you'll find the .po file. Edit this file and provide translations for the strings marked with msgid.
After adding translations, compile all the .po file into a machine-readable .mo file by running:
Use
python manage.py compilemessages
To compile specific language

### Use
python manage.py compilemessages -l <locale_code>
Note: When making messages from the template, be aware that Django will not consider words in the menu JSON file automatically. If making messages in the template provided language, remove the comment marks (#~) from the corresponding .po file, typically located at the bottom. Furthermore, if you've made changes to the menu JSON file and need translations for either the template's provided language or a new language, you'll need to manually update them in the .po file
At last add language to Navbar, language selection dropdown
Use
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
### data-language is the language code.
data-text-direction specifies the language's text direction, allowing you to set text direction for a specific language.
How to remove existing language?#
If you want to remove support for a language in your Django project:

Remove the language from the LANGUAGES setting in your settings.py file.
Delete the corresponding .po and .mo files for that language in the locale/<locale_code>/LC_MESSAGES/ directory.
Ensure that you update your views and templates to handle language fallbacks gracefully in case users have selected the removed language.
Remove language from language selection dropdown.

### Use
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
Run python manage.py compilemessages to regenerate the compiled .mo files for the remaining languages.
Using Translations in Template HTML Files#
Django provides a convenient way to translate text within HTML templates to support multiple languages. Here's how you can use translations in your template files:

### Loading the Translation Tags
Before using translation tags in your HTML templates, you need to load the {% load i18n %} tag at the top of your template. This tag loads the internationalization (i18n) template tags.

### Use
{% load i18n %}
Translating Text
To translate a piece of text, wrap it with the {% translate %} template tag. This tag marks the text for translation and will display the appropriate translation based on the user's selected language.

For example, to translate the text "Hello, World!" in your template:

### Use
<p>{% translate "Hello, World!" %}</p>
Refer to the translate template tag

Info: After adding the Translations in Template HTML Files, refer makemessages and compilemessages points from How to add new language?
Localization In Template Customizer#
We have also provided Localization in our Template Customizer. We have not handled Customizer's locale through Django but it is slightly interconnected.

When you change the template language using language dropdown from navbar. It'll also change the template customizer's language as per the selected language.

Internally, we have created a variable that is set as per the current Django language and sent this variable to our template-customizer.js file where we handle the customizer's localization.

Let's deep dive into it and understand how it works.

Internal variable to set Template Customizer's localization.

### Use
<script>
window.templateCustomizer = new TemplateCustomizer({
lang: '{{LANGUAGE_CODE}}',
  ...
});
</script>
customizer
We have a javascript object of languages where you have to put your translation for customizer in template-customizer.js file.

### Use
//  setting language
TemplateCustomizer.LANGUAGES = {
  en: {
    panel_header: 'TEMPLATE CUSTOMIZER',
    panel_sub_header: 'Customize and preview in real time',
    theming_header: 'THEMING',
    theme_header: 'THEME',
    theme_label: 'Themes',
    style_label: 'Style (Mode)',
    style_switch_light: 'Light',
    style_switch_dark: 'Dark',
    layout_header: 'LAYOUT',
    layout_label: 'Layout (Menu)',
    layout_static: 'Static',
    layout_offcanvas: 'Offcanvas',
    layout_fixed: 'Fixed',
    layout_fixed_offcanvas: 'Fixed offcanvas',
    layout_flipped_label: 'Menu flipped',
    layout_dd_open_label: 'Dropdown on hover',
    layout_navbar_label: 'Fixed navbar',
    layout_footer_label: 'Fixed footer',
    misc_header: 'MISC',
    rtl_label: 'RTL direction'
  },
  fr: {...},
  de: {...},
  ar: {...}
}
If you add or remove any language in Django then you have to add or remove the same language from the above Object. Otherwise, you'll get console errors.

If you don't want to use localization for customizer then you need to remove lang option from scripts_includes.html file:

### Use
<script>
window.templateCustomizer = new TemplateCustomizer({
lang: '{{LANGUAGE_CODE}}',
  ...
});
</script>
