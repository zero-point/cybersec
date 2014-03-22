#!/usr/bin/env python
# coding=UTF-8
#
# Python File.py
#
# Description
#

__author__      = "Donald Martin"
__license__     = "GPL"
__version__     = "0.1"
__maintainer__  = "Donald Martin"
__email__       = "donaldacmartin@gmail.com"
__status__      = "Development"

import os

def addLesson(title, img, points, desc, intro, imp, prev, iDemo):
    lesson = Lesson(title=title,
                    image=img,
                    award=points,
                    description=desc,
                    intro=intro,
                    implementation=imp,
                    prevention=prev,
                    implementDemo=iDemo,
                    preventDemo="")
    
    lesson.save()

def populate():
    addLesson("SQL Injection",
              "Lessons/injection.jpg",
              1000,
              "Injection flaws, such as SQL, OS, and LDAP injection occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.",
              "Injection flaws occur when an application sends untrusted data to an interpreter. Injection flaws are very prevalent, particularly in legacy code. They are often found in SQL, LDAP, Xpath, or NoSQL queries; OS commands; XML parsers, SMTP Headers, program arguments, etc. Injection flaws are easy to discover when examining code, but frequently hard to discover via testing. Scanners and fuzzers can help attackers find injection flaws.",
              "We will send simple text-based attacks that exploit the syntax of the targeted interpreter. Almost any source of data can be an injection vector, including internal sources.",
              "Sanitisation of text input can ensure that no SQL syntax is passed into your system.",
              "/pure-lesson-pages/sql-injection.html"
              )
              
    addLesson("Heuristics",
              "Lessons/fail.jpg",
              100,
              "While it is important to ensure that your code is secure, information sent back to the client could also pose a vulnerability to your system.",
              "lol",
              "lol",
              "lol",
              "lol"
              )
             
    addLesson("Insecure Direct Object References",
              "Lessons/lock.jpg",
              1000,
              "A direct object reference occurs when a developer exposes a reference to an internal implementation object, such as a file, directory, or database key. Without an access control check or other protection, attackers can manipulate these references to access unauthorized data.",
              "Direct object reference flaws result in objects and documents being unintentionally accessible as it is not properly protected. From the design perspective this usually means that requests can be made to specific objects without the authentication needed to reach this content. This usually is a result of web developers thinking that users will only seek content that is intended for them, which is where it starts to go wrong- even a simple Google search can give you access to confidential goverment documents- try entering the following to the search bar:       filetype:doc | filetype:pdf " + "this document is confidential"+ " site:gov  ",
              "This next demonstration assumes you have already logged into a sample bank system. As you will see, the database key is exposed in a URL and can be easily manipulated, granting access to information about other accounts, without proper authorisation",
              "The main weakness here is the access control. The application should always verify that this user is authorised to access that object once it involves sensitive content. Once you get this right, other mitigation techniques might seem redundant. However, depending on the context of your application, you might want to protect yourself from similar exploits. Don’t expose the actual ID/name of objects to the end user. And if for some reason you have to, something like an Indirect Reference Map can be used to create alternative keys for application side objects, such that the original database keys are never visible.  This should also minimize user ability to predict object keys if done neatly",
              "/pure-lesson-pages/insecure-objects.html"
              )
              
    addLesson("Sensitive Data",
              "Lessons/Feather1.jpg",
              500,
              "A lesson on sensitive data.",
              "lol",
              "lol",
              "lol",
              "/pure-lesson-pages/sensitive-data-continuance.html"
              )
              
    addLesson("Cross-Site Scripting",
              "Lessons/3_1.jpg",
              1000,
              "Often abbreviated as “XSS”, it is a type of computer security vulnerability typically found in Web applications. It enables attackers to inject client-side script into Web pages viewed by other users. Their effect may range from a petty nuisance to a significant security risk, depending on the sensitivity of the data handled by the vulnerable site and the nature of any security mitigation implemented by the site's owner.",
              "Cross-site scripting (XSS) is a code injection attack that allows an attacker to execute malicious JavaScript in another user's browser.\n\nThe attacker does not directly target his victim. Instead, he exploits a vulnerability in a website that the victim visits, in order to get the website to deliver the malicious JavaScript for him. To the victim's browser, the malicious JavaScript appears to be a legitimate part of the website, and the website has thus acted as an unintentional accomplice to the attacker.",
              "The only way for the attacker to run his malicious JavaScript in the victim's browser is to inject it into one of the pages that the victim downloads from the website. This can happen if the website directly includes user input in its pages, because the attacker can then insert a string that will be treated as code by the victim's browser.",
              "In order to prevent this type of code injection, secure input handling is needed. For a web developer, there are two fundamentally different ways of performing secure input handling: validation and encoding. Validation, which filters the user input so that the browser interprets it as code without malicious commands. Encoding, which escapes the user input so that the browser interprets it only as data, not as code.",
              "/pure-lesson-pages/cross-site-scripting.html"
              )
              
    addLesson("Cross-Site Request Forgery",
              "Lessons/csrf_1.png",
              1000,
              "A CSRF attack forces a logged-on victim’s browser to send a forged HTTP request, including the victim’s session cookie, to a vulnerable web application. This allows the attacker to force the victim’s browser to generate requests the vulnerable application thinks are legitimate requests from the victim. A successful exploit can compromise end user data and operations in the case of normal users. If the targeted end user is the administrator account, this can compromise the entire web application.",
              "This form of attack takes advantage of the fact that most web apps allow attackers to predict all the details of a particular action. Because browsers send credentials like session cookies automatically, attackers can create malicious web pages which generate forged requests that are indistinguishable from legitimate ones.",
              "The attacker can create forged HTTP requests and trick a victim into submitting them via image tags, XSS, or numerous other techniques. If the user is authenticated, the attack succeeds.",
              "Preventing CSRF usually requires the inclusion of an unpredictable token in each HTTP request. Such tokens should, at a minimum, be unique per user session. The preferred option is to include the unique token in a hidden field. This causes the value to be sent in the body of the HTTP request, avoiding its inclusion in the URL, which is more prone to exposure.\n\nThe unique token can also be included in the URL itself, or a URL parameter. However, such placement runs a greater risk that the URL will be exposed to an attacker, thus compromising the secret token. Requiring the user to re-authenticate, or prove they are a user (e.g., via a CAPTCHA).",
              "/pure-lesson-pages/cross-site-request-forgery.html"
              )
              
    addLesson("Broken Authentication and Session Management",
              "Lessons/Authentification_1.jpg",
              100,
              "Broken Authentication and Session Management is one of those common web application vulnerabilities which are less known but dangerous. According OWASP, this vulnerability is third most found vulnerability on the web application. This is quite a broad field, however most commonly exploited issue is found in the web applications where developers fail to protect users’ session information.",
              "Authenticating to a website is something most of us probably do multiple times every day. Look at your open tabs right now! You probably have your Facebook, GitHub, some email client open? Each one these individually authenticated to.\n\nAs a developer, it is your duty to secure both, your users current session and any persistent data – such as credentials. If a hacker can get a hold of users session ID, he can replicate it in a URL or a cookie and effectively become his victim without needing a username or password.\n\nIn this lesson we shall be focusing some key points:\n\nUnsecure and easily accessible Session ID's, weak security in forgotten password, remember my password, account update, and other related functions",
              "In this example we will be getting past the mock login componet and login in as our victim. We will be exploiting the fact that this application does not use cokies to hold the session ID it can be easily obtained to mimic our victim and get past the authentification.",
              "Since there is a trade off between security and usability of application, you can never prevent Broken Authentication or Session theft completely (would you like this site to remember and autocomplete your login/password?).\n\nHowever, we can mitigate most of these flaws by putting some good engineering practices in place:\nAvoid cookieless sessions\nDo not try to build an authentification system yourself unless you have to\nExpire sessions early and often(depending on sensitivity of the user data your application will hold)\nUse unique session IDs everytime (do not re use the same ID)\nAdd IP checking\nDouble check passwords or other security information on certain activities(ex bank transfer)\nUse SSL",
              "/pure-lesson-pages/stolen-session-demo.html",
              )
              
if __name__ == "__main__":
    print("Starting population script")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn.settings")
    from course.models import Lesson
    populate()
