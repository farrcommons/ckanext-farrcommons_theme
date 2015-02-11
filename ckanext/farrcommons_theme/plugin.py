import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer
from ckan.plugins import IRoutes

class FarrCommonsThemePlugin(plugins.SingletonPlugin):
    '''The FarrCommons theme plugin.

    '''
     # Declare that this class implements IConfigurer.
    implements(IConfigurer, inherit=True)
    implements(IRoutes, inherit=True)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        #toolkit.add_template_directory(config, 'templates')
        # set the title
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))
        our_public_dir = os.path.join(rootdir, 'ckanext',
                                      'farrcommons_theme', 'public')
        template_dir = os.path.join(rootdir, 'ckanext',
                                    'farrcommons_theme', 'templates')
        # set our local template and resource overrides
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
            config.get('extra_template_paths', '')])

        config['ckan.site_title'] = "Farr Commons"
        # set the logo
        config['ckan.site_logo'] = 'images/logo.png'
