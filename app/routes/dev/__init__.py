from flask_classful import FlaskView, route


class DevRoute(FlaskView):
    @route('/logout/', methods=['GET', 'POST'])
    def logout(self):
        return redirect("/", code=302)