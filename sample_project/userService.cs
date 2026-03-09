public class UserService
{
    public void SaveUser(User user)
    {
        Database db = null;
        db.Save(user);
    }
}