#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

from BaseRunner import BaseRunner


class maple(BaseRunner):
    def __init__(self):
        super().__init__("maple", maple)

        self.url = "git@github.com:ICBench/maple.git"

    def prepare_run_cb(self, tmp_dir, params):

    def get_version_cmd(self):
        return [self.executable, "-version"]

    def get_version(self):
        version = super().get_version()

        return " ".join([self.name, version.split()[2]])
