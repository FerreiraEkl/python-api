from config import *


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    cpf = db.Column(db.String(254))

    def __str__(self):
        return self.nome + "[id="+str(self.id) + "], " + self.email + ", " + self.cpf

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf
        }


class Disciplina (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    ementa = db.Column(db.String(254))
    cargaHoraria = db.Column(db.Integer)

    def __str__(self):
        return f"{self.nome} [{self.id}], unidade={self.ementa} ({self.cargaHoraria})"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "unidade": self.ementa,
            "vr": self.cargaHoraria
        }


class EstudanteDaDisciplina (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.Integer)
    frequencia = db.Column(db.Integer)
    mediaFinal = db.Column(db.Integer)

    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")

    disciplina_id = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False)
    disciplina = db.relationship("Disciplina")

    def __str__(self):
        return f"{self.semestre}, {self.frequencia}, {self.mediaFinal} " + f"{self.pessoa}, {self.disciplina}"

    def json(self):
        return {
            "id": self.id,
            "semestre": self.semestre,
            "frequencia": self.frequencia,
            "mediaFinal": self.mediaFinal,
            "pessoa_id": self.pessoa_id,
            "pessoa": self.pessoa.json(),
            "disciplina_id": self.disciplina_id,
            "disciplina": self.disciplina.json()
        }


if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()