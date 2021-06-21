# Bash: when in a git repository, show the current branch, indicate if the working directory is clean or not.
function __set_my_prompt
{
   local RED="\033[0;31m"
   local GREEN="\033[0;32m"
   local NOCOLOR="\033[0m"
   local YELLOW="\033[0;33m"
   local BLACK="\033[0;30m"

   local git_modified_color="\[${GREEN}\]"
   local git_status=$(git status | grep "Your branch is ahead" 2>/dev/null)
   if [ "$git_status" != "" ]
   then
       git_modified_color="\[${YELLOW}\]"
   fi
   local git_status=$(git status --porcelain 2>/dev/null)
   if [ "$git_status" != "" ]
   then
       git_modified_color="\[${RED}\]"
   fi

   local git_branch=$(git branch 2>/dev/null | sed 's/^..//')
   if [ "$git_branch" != "" ];
   then
      git_branch="($git_modified_color$git_branch\[${BLACK}\]) "
   fi
   PS1="\[${BLACK}\]\u@\h \w $git_branch$\[${NOCOLOR}\] "
}

PROMPT_COMMAND='__set_my_prompt'
