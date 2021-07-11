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
import os


class maple(BaseRunner):
    def __init__(self):
        super().__init__("maple", "maple")

        self.url = "https://github.com/ICBench/maple"

    def prepare_run_cb(self, tmp_dir, params):
        run = os.path.join(tmp_dir, "run.tcl")
        flist = os.path.join(tmp_dir, "flist")

        defs = "-define SYNTHESIS "
        with open(flist, 'w') as f:
            for incdir in params['incdirs']:
                f.write(f'+incdir+{incdir}\n')
                print(f'+incdir+{incdir}')
            for i in reversed(params['files']):
                f.write(i + "\n")

        for define in params['defines']:
            defs += f' -define {define} '

        with open(run, 'w') as f:
            f.write('set_runtime_flag db_allow_external_nets 1\n')
            f.write(f'read -dont_clean -f {flist} {defs}\n')

        self.cmd = [self.executable, '-script_file', run]
