# Copyright 2015 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from tripleo.common import scale

LOG = logging.getLogger(__name__)


def get_group_resources_after_delete(groupname, res_to_delete, resources):
    LOG.warn('tripleo_common.scale.get_group_resources_after_delete is' +
             'deprecated, please use ' +
             'tripleo.common.scale.get_group_resources_after_delete')
    scale.get_group_resources_after_delete(groupname, res_to_delete, resources)


class ScaleManager(scale.ScaleManager):
    def __init__(self, **kwargs):
        LOG.warn('tripleo_common.scale.ScaleManager is deprecated, ' +
                 'please use tripleo.common.scale.ScaleManager')
        scale.ScaleManager.__init__(self, **kwargs)
