Django rest framework test application.

<p>$docker build -t quiz-docker -f Dockerfile . / $docker-compose build </p>
<p>$docker-compose up -d</p>

<h5>Instruction</h5>
<p>For admin:</p>
<p>1. Get token for autorization in system: /api/v1/gettoken/, with data 'username' and 'password'. </p>
<p>2. Create new quiz (token required): /api/v1/quiz/new/, available data 'title'(required), 'description', 'date_finish', 'questions'(id). </p>
<p>3. Update and delete quiz (token required): /api/v1/quiz/{int:id}/, int:id - quiz pk.</p>
<p>4. Quiz list: /api/v1/quiz/all/. Filters by 'title' and 'description' are available (example /api/v1/quiz/all/?title__contains=q&description__contains=b) </p>
<p>5. Question list (token required): /api/v1/question/all/. </p>
<p>6. Create new question (token required): /api/v1/question/new/, available data 'text'(required), 'qtype'(required), there are 3 types: text(1), choose one(2), choosemany(3), 'choices'(required if qtype 2 or 3). </p>
<p>7. Update and delete question (token required): /api/v1/question/{int:id}/, int:id - question pk.</p>
<p>There are no functions for choices(no needed). It can be created similarly as quiz and question. </p>
<p>There is no functions for all passed quizzes(no neede). It can be created similarly as point 11. </p>
<p>*****</p>
<p>For user:</p>
<p>Registration no needed, app will provide identification id. </p>
<p>8. Quiz list: /api/v1/quiz/all/. Filters by 'title' and 'description' are available (example /api/v1/quiz/all/?title__contains=q&description__contains=b) </p>
<p>9. Create new user: /api/v1/new_user/, with no data, app will provide id, looks like "8f2d55e098ce0fe8b8620f4bdbe12295847a23f3", use it for work with app. </p>
<p>10. Pass quiz: /api/v1/{str:uuid}/quiz/{int:quiz}/question/{int:question}/{str:answer}/ : {str:uuid} - user id (point 2), {int:quiz} and {int:question} - quiz and question id, {str:answer} - question answer. </p>
<p>11. Passed quiz list by user id: /api/v1/{str:uuid}/quiz/all/,  {str:uuid} - user id (point 2). </p>
