remove_array_dups() {
  # Usage: remove array duplicates
  #
  declare -A tmp_array

  for i in "$@"; do
    [[ $i ]] && IFS=" " tmp_array["${i:-}"]=1 
  done

  printf '%s\n' "${!tmp_array[@]}"
}
