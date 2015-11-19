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

from tripleo.common import stack_update

LOG = logging.getLogger(__name__)


class StackUpdateManager(stack_update.StackUpdateManager):
    def __init__(self, heatclient, novaclient, stack, hook_type,
                 nested_depth=5, hook_resource=None):
        LOG.warn('tripleo_common.stack_update.StackUpdateManager is ' +
                 'deprecated, please use ' +
                 'tripleo.common.stack_update.StackUpdateManager')
        stack_update.StackUpdateManager.__init__(self, heatclient,
                                                 novaclient, stack,
                                                 hook_type, nested_depth,
                                                 hook_resource)
