 #
 # Copyright 2004 Apache Software Foundation
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you
 # may not use this file except in compliance with the License.  You
 # may obtain a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 # implied.  See the License for the specific language governing
 # permissions and limitations under the License.
 #
 # Originally developed by Gregory Trubetskoy.
 #
 # $Id: python22.py 374268 2006-02-02 05:31:45Z nlehuen $

# This file contains a bunch of hacks used to support Python 2.2

import sys
if sys.version < '2.3':
    import __builtin__ as hack
    
    # Enumerate does not exists in Python 2.2
    hack.enumerate = lambda s : zip(xrange(len(s)),s)
