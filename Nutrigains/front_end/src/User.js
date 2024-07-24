export class User {
    static emailId = "";
    static setEmailId(emailId){
        User.emailId = emailId;
    }
    static getEmailId(){
        return User.emailId;
    }
}