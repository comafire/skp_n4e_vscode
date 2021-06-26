#!/bin/bash

eval "$(direnv hook bash)"

#echo $@
invoke -e -r $VSCODE_HOME/src/tasks "$@"
