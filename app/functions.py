from datetime import datetime
import pytz

def turno_atual(return_int=False):
    tz = pytz.timezone('America/Sao_Paulo')
    hora_atual = datetime.now(tz).hour
    if 6 <= hora_atual < 12:
        return 'manha' if not return_int else 1
    elif 12 <= hora_atual < 18:
        return 'tarde' if not return_int else 2
    elif 18 <= hora_atual < 22:
        return 'noite' if not return_int else 3
    else:
        return 'madrugada' if not return_int else 0

turno_atual()


"""sugestao para a classe agendamentos, implementando funções extra que serão necessarias """


"""

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    ID_agendamento = db.Column(db.Integer, primary_key=True)
    TimeStamp_inicio = db.Column(db.DateTime, nullable=False)
    ID_locatario = db.Column(db.Integer, nullable=False)
    Tipo_locatario = db.Column(db.String(50), nullable=False)
    ID_turma = db.Column(db.Integer, db.ForeignKey('turmas.ID_turma'))
    TimeStamp_fim = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Agendamento {self.ID_agendamento}>'

    # Função de criação de agendamento (mantida)
    @classmethod
    def criar_agendamento(cls, timestamp_inicio, id_locatario, tipo_locatario, id_turma, timestamp_fim):
        novo_agendamento = cls(TimeStamp_inicio=timestamp_inicio, ID_locatario=id_locatario,
                               Tipo_locatario=tipo_locatario, ID_turma=id_turma, TimeStamp_fim=timestamp_fim)
        db.session.add(novo_agendamento)
        db.session.commit()
        return novo_agendamento

    # Listar todos os agendamentos (mantido)
    @classmethod
    def listar_agendamentos(cls):
        return cls.query.all()

    # 1. Validação de Disponibilidade de Sala
    @classmethod
    def validar_disponibilidade(cls, timestamp_inicio, timestamp_fim, id_turma):
        conflito = cls.query.filter(
            cls.ID_turma == id_turma,
            cls.TimeStamp_inicio < timestamp_fim,
            cls.TimeStamp_fim > timestamp_inicio
        ).first()
        return conflito is None  # Se não houver conflitos, a sala está disponível

    # 2. Gerenciamento de Horários Recorrentes
    @classmethod
    def criar_agendamento_recorrente(cls, timestamp_inicio, id_locatario, tipo_locatario, id_turma, timestamp_fim, frequencia, repeticoes):
        agendamentos = []
        for _ in range(repeticoes):
            if cls.validar_disponibilidade(timestamp_inicio, timestamp_fim, id_turma):
                novo_agendamento = cls.criar_agendamento(timestamp_inicio, id_locatario, tipo_locatario, id_turma, timestamp_fim)
                agendamentos.append(novo_agendamento)
                # Incrementar o timestamp_inicio e timestamp_fim com base na frequência
                timestamp_inicio += frequencia
                timestamp_fim += frequencia
            else:
                break
        return agendamentos

    # 3. Listagem de Agendamentos por Sala
    @classmethod
    def listar_agendamentos_por_sala(cls, id_turma, data_inicio=None, data_fim=None):
        query = cls.query.filter_by(ID_turma=id_turma)
        if data_inicio and data_fim:
            query = query.filter(cls.TimeStamp_inicio >= data_inicio, cls.TimeStamp_fim <= data_fim)
        return query.all()

    # 4. Listagem de Agendamentos por Turma
    @classmethod
    def listar_agendamentos_por_turma(cls, id_turma):
        return cls.query.filter_by(ID_turma=id_turma).all()
"""