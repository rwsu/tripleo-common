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

from tripleo.common import update

LOG = logging.getLogger(__name__)


def add_breakpoints_cleanup_into_env(env):
    LOG.warn('tripleo_common.update.add_breakpoints_cleanup_into_env is ' +
             'deprecated, please use ' +
             'tripleo.common.update.add_breakpoints_cleanup_into_env')
    update.add_breakpoints_cleanup_into_env(env)


class PackageUpdateManager(update.PackageUpdateManager):
    def __init__(self, heatclient, novaclient, stack_id,
                 tht_dir=None, environment_files=None):
        LOG.warn('tripleo_common.update.PackageUpdateManager is ' +
                 'deprecated, please use ' +
                 'tripleo.common.update.PackageUpdateManager')
        update.PackageUpdateManager.__init__(self, heatclient, novaclient,
                                             stack_id, tht_dir,
                                             environment_files)
