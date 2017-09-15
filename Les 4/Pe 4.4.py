def newpassword(oldpassword, newpassword):
  if oldpassword != newpassword and len(newpassword) >= 6:
    if any( char.isdigit() for char in newpassword):
        return True
    else:
        return False
  else:
    return False
print(newpassword("rode123", "Banaan"))
