-- privileges!
USERS=("user_0d_1" "user_0d_2")

# Loop through each user and retrieve privileges
for USER in "${USERS[@]}"; do
    echo "Privileges for $USER:"

    # Query MySQL server for privileges
    mysql -u $USER -p -e "SHOW GRANTS;" | grep "GRANT"

    echo "-------------------------------------"
done
