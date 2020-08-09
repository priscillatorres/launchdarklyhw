import ldclient
if __name__ == "__main__":
  ldclient.set_sdk_key("sdk-0ebb2bd7-80bd-47da-bc49-7a98d8ad5771")

  user = {
  "key": "UNIQUE IDENTIFIER",
  "firstName": "Bob",
  "lastName": "Loblaw",
  "custom": {
    "groups": "beta_testers"
  }
}

show_feature = ldclient.get().variation("park-default-sortorder", user, False)

if show_feature:
  print("Showing your feature")
else:
  print("Not showing your feature")

ldclient.get().close()
