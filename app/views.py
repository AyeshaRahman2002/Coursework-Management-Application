from app import app,db,models
from .forms import AssessmentForm, searchForm
from flask import render_template, flash, redirect, request

#Creating a route for All Assessments page attaching index.html to it
@app.route('/')
def index():
    with app.app_context():
        q = request.args.get('q')
        if q:
            AllAssessments = models.AssessmentForm.query.filter(AssessmentForm.ModuleCode.contains(q) | AssessmentForm.body.contains(q))   #for search button
        else:
            AllAssessments = models.AssessmentForm.query.all()
    return render_template('index.html',  ModuleTitle = "All Assessments",  AllAssessments=AllAssessments)

#Creating a route for creating an assignment and then storing it in a database from where it is put in the incomplete assessments page
@app.route('/Creating', methods=['GET', 'POST', 'PUT'])
def Creating():
     form = AssessmentForm()
     if form.validate_on_submit():
         flash('%s has been successfully added.'%(form.Module.data))
         with app.app_context():
              Creating = models.AssessmentForm(ModuleTitle = form.Title.data , ModuleCode = form.Module.data, ModuleDeadline = form.Deadline.data, ModuleDescription = form.Description.data)
              db.session.add(Creating)
              db.session.commit()
              return redirect("/Incomplete")
     return render_template('Creating.html', ModuleTitle='Create Assessments', form=form)

#Creating a route for assignments which are marked completed. To do this it checks if the value is true or not and then displays it depending on whether it is completed or not
@app.route('/Completed')
def Completed():
     with app.app_context():
         Completed = models.AssessmentForm.query.filter_by(ModuleCompleted=True).all()
     return render_template('Completed.html', ModuleTitle = "Complete Assessments", Completed=Completed)

#Creating a "updated" route for ModuleID. This is used to update the assessments when it is completed 
@app.route('/<int:ModuleID>', methods=['GET', 'POST', 'PUT'])
def Updated(ModuleID):
    with app.app_context():
         UpdatedAssessments = models.AssessmentForm.query.get(ModuleID)
         if request.method == 'POST':
             UpdatedAssessments.ModuleCompleted =True
             db.session.commit()
         return redirect("/Completed")   

#Creating a route for incomplete assessments. This checks if the value is false and displays it depending on whether it is incomplete or not
@app.route('/Incomplete')     
def Incomplete():
     with app.app_context():
         IncompleteAssessments = models.AssessmentForm.query.filter_by(ModuleCompleted=False).all()
     return render_template('Incomplete.html', ModuleTitle = "Incomplete Assessments", IncompleteAssessments = IncompleteAssessments)    

#Creating a delete button to delete the created assignment
@app.route('/Delete/<int:ModuleID>', methods=['GET','POST'])
def Delete(ModuleID):
    with app.app_context():
        form = AssessmentForm()
        DeleteAssignment = models.AssessmentForm.query.get_or_404(ModuleID)
        if request.method == "POST":
            db.session.delete(DeleteAssignment)
            db.session.commit()
        flash('%s has been deleted.'%(form.Module.data))  
        return redirect("/")


#Creating a route for searched assessments. This displays the assessment bases on the module code entered in the search field & displays the mark complete or delete or both button as per there status
@app.route('/search', methods=["POST"])
def Search():
    form = searchForm()
    searchedAssessment = models.AssessmentForm.query.filter_by(ModuleCode=form.searched.data).all()
    return render_template('search.html', form=form, searched=form.searched.data, searchedAssessment=searchedAssessment)