"""
" Copyright:    Loggly
" Author:       Scott Griffin
" Last Updated: 09/19/2014
"
" Configuration file for loggly's internal analytics data snapshotting consumer routines.
"
"""
import os
from os.path import abspath, join
#from ..config import ENV, root_dir
from config_load import config_loader

class Config(object):
    debug            = False
    sfdc_source_name = 'Product'

##class ProdConfig( Config ):
##    database = {
##        'dialect'           : 'mysql',
##        'host'              : 'analytics-db.loggly.com',
##        'user'              : 'migration',
##        'password'          : 'M1gration4L1f3',
##        'dbname'            : 'analytics_chopper_staging'
##    }
##
##    marketo_ini     = '/etc/analytics/loggly_marketo.ini'
##    kissmetrics     = config_loader( '/etc/analytics/kissmetrics.py' )
##    sfdc_env        = 'prod'
##
##class DevConfig( ProdConfig ):
##    debug = True
##
##    database = {
##        'dialect'           : 'mysql',
##        'host'              : 'analytics-db.loggly.com',
##        'user'              : 'migration',
##        'password'          : 'h00verl0ggly!',
##        'dbname'            : 'analytics_dev'
##    }
##
##    marketo_ini     = '/etc/analytics/sandbox_marketo.ini'
##    kissmetrics     = config_loader( '/etc/analytics/kissmetrics_sandbox.py' )
##    sfdc_env        = 'sandbox'
##
##class UniboxConfig( ProdConfig ):
##    debug = True
##
##    database = {
##        'dialect'           : 'mysql',
##        'host'              : 'localhost',
##        'user'              : 'uniboxuser',
##        'password'          : 'Unib0xMe!',
##        'dbname'            : 'analyticsdb_unibox'
##    }
##
##    marketo_ini     = '/etc/analytics/sandbox_marketo.ini'
##    kissmetrics     = config_loader( '/etc/analytics/kissmetrics_sandbox.py' )
##    sfdc_env        = 'sandbox'
##
##class TestConfig( ProdConfig ):
##    debug = False
##
##    database = {
##        'dialect'           : 'mysql',
##        'host'              : 'localhost',
##        'user'              : 'unittest',
##        'password'          : 'unittest',
##        'dbname'            : 'analytics_unit_test',
##        'schema'            : join( root_dir, '..', 'analyticsdb', 'schema', 'analyticsdb_chopper.sql' )
##    }
##
##
##    marketo_ini     = '/etc/analytics/sandbox_marketo.ini'
##    kissmetrics     = config_loader( '/etc/analytics/kissmetrics_test.py' )
##    sfdc_env        = 'sandbox'

class MyConfig(Config):
    debug = True

    marketo         =    config_loader( 'marketo_test1.py' )
    sfdc_env        = 'sandbox'


root_dir = os.path.abspath( os.path.dirname( __file__ ) )


ENV = os.environ.get( 'ANALYTICS_SYNC' )
if not ENV:
    prod_systems = (
        'analytics01',
    )

    unibox_systems = (
        'scott.uni.loggly.net',
    )

    dev_systems = (
        'Scotts-MacBook-Pro.local',
    )

    _, nodename, _, _, _ = os.uname()
##    if nodename in prod_systems:
##        ENV = 'PROD'
##    if nodename in unibox_systems:
##        ENV = 'UNIBOX'
##    else:
    ENV = 'DEV'


'''if 'DEV' == ENV:
    CONFIG = DevConfig
elif 'UNIBOX' == ENV:
    CONFIG = UniboxConfig
elif 'TEST' == ENV:
    CONFIG = TestConfig
elif 'PROD' == ENV:
    CONFIG = ProdConfig'''

CONFIG = MyConfig 
