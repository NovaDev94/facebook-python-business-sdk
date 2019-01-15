# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class PageCallToAction(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPageCallToAction = True
        super(PageCallToAction, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        android_app = 'android_app'
        android_deeplink = 'android_deeplink'
        android_destination_type = 'android_destination_type'
        android_package_name = 'android_package_name'
        android_url = 'android_url'
        created_time = 'created_time'
        email_address = 'email_address'
        field_from = 'from'
        id = 'id'
        intl_number_with_plus = 'intl_number_with_plus'
        iphone_app = 'iphone_app'
        iphone_deeplink = 'iphone_deeplink'
        iphone_destination_type = 'iphone_destination_type'
        iphone_url = 'iphone_url'
        status = 'status'
        type = 'type'
        updated_time = 'updated_time'
        web_destination_type = 'web_destination_type'
        web_url = 'web_url'

    class AndroidDestinationType:
        website = 'WEBSITE'
        app_deeplink = 'APP_DEEPLINK'
        facebook_app = 'FACEBOOK_APP'
        phone_call = 'PHONE_CALL'
        messenger = 'MESSENGER'
        email = 'EMAIL'
        shop_on_facebook = 'SHOP_ON_FACEBOOK'
        none = 'NONE'

    class IphoneDestinationType:
        website = 'WEBSITE'
        app_deeplink = 'APP_DEEPLINK'
        facebook_app = 'FACEBOOK_APP'
        phone_call = 'PHONE_CALL'
        messenger = 'MESSENGER'
        email = 'EMAIL'
        shop_on_facebook = 'SHOP_ON_FACEBOOK'
        none = 'NONE'

    class Type:
        book_now = 'BOOK_NOW'
        call_now = 'CALL_NOW'
        charity_donate = 'CHARITY_DONATE'
        contact_us = 'CONTACT_US'
        donate_now = 'DONATE_NOW'
        message = 'MESSAGE'
        open_app = 'OPEN_APP'
        play_now = 'PLAY_NOW'
        shop_now = 'SHOP_NOW'
        sign_up = 'SIGN_UP'
        watch_now = 'WATCH_NOW'
        get_offer = 'GET_OFFER'
        get_offer_view = 'GET_OFFER_VIEW'
        request_quote = 'REQUEST_QUOTE'
        book_appointment = 'BOOK_APPOINTMENT'
        listen = 'LISTEN'
        email = 'EMAIL'
        learn_more = 'LEARN_MORE'
        request_appointment = 'REQUEST_APPOINTMENT'
        get_directions = 'GET_DIRECTIONS'
        buy_tickets = 'BUY_TICKETS'
        play_music = 'PLAY_MUSIC'
        visit_group = 'VISIT_GROUP'
        shop_on_facebook = 'SHOP_ON_FACEBOOK'
        local_dev_platform = 'LOCAL_DEV_PLATFORM'
        interested = 'INTERESTED'
        woodhenge_support = 'WOODHENGE_SUPPORT'

    class WebDestinationType:
        email = 'EMAIL'
        messenger = 'MESSENGER'
        none = 'NONE'
        website = 'WEBSITE'
        shop_on_facebook = 'SHOP_ON_FACEBOOK'
        become_supporter = 'BECOME_SUPPORTER'

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageCallToAction,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'type': 'type_enum',
            'intl_number_with_plus': 'string',
            'email_address': 'string',
            'web_destination_type': 'web_destination_type_enum',
            'web_url': 'string',
            'android_destination_type': 'android_destination_type_enum',
            'android_deeplink': 'string',
            'android_package_name': 'string',
            'android_url': 'string',
            'android_app_id': 'int',
            'iphone_destination_type': 'iphone_destination_type_enum',
            'iphone_deeplink': 'string',
            'iphone_url': 'string',
            'iphone_app_id': 'int',
        }
        enums = {
            'type_enum': PageCallToAction.Type.__dict__.values(),
            'web_destination_type_enum': PageCallToAction.WebDestinationType.__dict__.values(),
            'android_destination_type_enum': PageCallToAction.AndroidDestinationType.__dict__.values(),
            'iphone_destination_type_enum': PageCallToAction.IphoneDestinationType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PageCallToAction,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'android_app': 'Application',
        'android_deeplink': 'string',
        'android_destination_type': 'string',
        'android_package_name': 'string',
        'android_url': 'string',
        'created_time': 'datetime',
        'email_address': 'string',
        'from': 'Page',
        'id': 'string',
        'intl_number_with_plus': 'string',
        'iphone_app': 'Application',
        'iphone_deeplink': 'string',
        'iphone_destination_type': 'string',
        'iphone_url': 'string',
        'status': 'string',
        'type': 'string',
        'updated_time': 'datetime',
        'web_destination_type': 'string',
        'web_url': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AndroidDestinationType'] = PageCallToAction.AndroidDestinationType.__dict__.values()
        field_enum_info['IphoneDestinationType'] = PageCallToAction.IphoneDestinationType.__dict__.values()
        field_enum_info['Type'] = PageCallToAction.Type.__dict__.values()
        field_enum_info['WebDestinationType'] = PageCallToAction.WebDestinationType.__dict__.values()
        return field_enum_info


