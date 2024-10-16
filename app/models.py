from app import db

class AssessmentForm(db.Model):
    ModuleDeadline = db.Column(db.Date)

    ModuleTitle = db.Column(db.String(200))
    
    ModuleDescription = db.Column(db.String(200))
    
    ModuleCode = db.Column(db.String(200), index=True)
    
    ModuleID = db.Column(db.Integer, primary_key=True)
    
    ModuleCompleted = db.Column(db.Boolean, default= False)

    def __repr__(self):
        return self.name