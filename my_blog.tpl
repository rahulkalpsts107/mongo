<!DOCTYPE html>
<html>
<head>
<title> Welcome to {{owner}} Blog</title>
<body>
<h1>Hi {{username}} , Welcome to my blog !!</h1>
<a href = "https://www.google.com/search?q=rahul+ramesh" color = "red">Google about Author</a><br/><br/><br/><br/><br/>
<b> My Blogs are </b>
<ul>
%for blog in blogs:
<li>{{blog}}</li>
%end
</ul>
<br/><br/><br/>
<h3>Add to My Mailing List For Updates!</h3>
<form action = "/subscribed" method = "POST">
Enter your Email to Subscribe
<input type="text" name ="emailid" size = "50" value ="" /><br/>
<input type="hidden" name ="usn" size = "50" value ={{username}} /><br/>
<input type="submit" value ="Subscribe" /><br/>
</form>
</body>
</html>