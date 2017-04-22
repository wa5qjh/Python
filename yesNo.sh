#!/usr/bin/env bash
# How do you use this code?
getyn='( while read yn
 do
  case "$yn" in
      y|Y|YES|yes) exit 0 ;;
      n|N|no|NO)   exit 1 ;;
      *) echo "Please answer y or n" >&2 ;;
  esac
 done )'

pause='( echo -n "Pause: "; read X; )';