from flask import Flask, render_template, url_for
from flask_wtf import Form
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class MyForm(Form):
    lang = SelectField(u'Website', 
                choices=[('', ''), ('chambre', 'Chambre'), ('salon', 'Salon'), 
                         ('cuisine', 'Cuisine'),('salle de bain','Bain')], 
                      id = 'selectmenu')
    submit = SubmitField('Go')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

posts = [
    {
        'marque': "Traitement d'images",
        'titre': "Dedoublement de mail et analyse des images d'annonce immobilière.",
        'content': "\nNous avons chercher à comparer les images entre elles pour voir leur ressemblances. Dans un premier temps nous avons utiliser compare_ssim et ensuite SIFT. \n Ensuite nous avons utiliser Mask RCNN et la dataset de COCO pour identifer les différentes pièces que le bien possède."
    },
    {
        'marque': 'Fonctionnement du site',
        'titre': '',
        'content': "Cliquer sur les onglets en haut de la page pour accéder aux différents liens du site."
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/dedoublement')
def index(): 
    return render_template('dedoublement.html',title='Dedoublement_mail')


@app.route('/piece')
def piece(): 
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/piece/'+form.lang.data)
    return render_template('piece.html',title='Identification_pieces',form=form)

@app.route("/piece/Chambre")
def chambre():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/piece/'+form.lang.data)
    return render_template('chambre.xhtml', title='Identification objet dans une chambre', form=form)

@app.route("/piece/Salon")
def salon():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/piece/'+form.lang.data)
    return render_template('salon.xhtml', title='Identification objet dans un salon', form=form)

@app.route("/piece/Cuisine")
def cuisine():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/piece/'+form.lang.data)
    return render_template('cuisine.xhtml', title='Identification objet dans une cuisine', form=form)

@app.route("/piece/Bain")
def bain():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/piece/'+form.lang.data)
    return render_template('bain.xhtml', title='Identification objet dans une salle de bain', form=form)


if __name__ == '__main__':
    app.run(debug=True)