from django.db import models

# Modelo Ativo (Equipamento)
# Baseado na descrição textual e no Diagrama de Classe.
class Ativo(models.Model):
    """
    Representa os ativos da empresa, como veículos, motores e outras máquinas.
    """
    # Enumeração para Tipo de Ativo, conforme o diagrama.
    class TipoAtivoChoices(models.TextChoices):
        VEICULO = 'VEICULO', 'Veículo'
        MOTOR = 'MOTOR', 'Motor'
        OUTROS = 'OUTROS', 'Outros'

    # Enumeração para Tipo de Contador, conforme o diagrama.
    class TipoContadorChoices(models.TextChoices):
        HODOMETRO = 'HODOMETRO', 'Hodômetro'
        HORIMETRO = 'HORIMETRO', 'Horímetro'

    # Atributos do modelo Ativo
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    tipo_ativo = models.CharField(
        max_length=10,
        choices=TipoAtivoChoices.choices,
        default=TipoAtivoChoices.OUTROS,
        verbose_name="Tipo de Ativo"
    )
    data_fabricacao = models.DateField(verbose_name="Data de Fabricação", null=True, blank=True)
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição")
    tipo_contador_principal = models.CharField(
        max_length=10,
        choices=TipoContadorChoices.choices,
        verbose_name="Tipo de Contador Principal"
    )
    hodometro_inicial = models.FloatField(default=0, verbose_name="Hodômetro Inicial/Atual")
    horimetro_inicial = models.FloatField(default=0, verbose_name="Horímetro Inicial/Atual")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"


# Modelo ManutencaoProgramada
# Baseado na descrição textual e no Diagrama de Classe.
class ManutencaoProgramada(models.Model):
    """
    Armazena as programações de manutenções para os ativos.
    """
    # Enumerações para Tipo e Status da Manutenção, conforme o diagrama.
    class TipoManutencaoChoices(models.TextChoices):
        PREVENTIVA = 'PREVENTIVA', 'Preventiva'
        CORRETIVA = 'CORRETIVA', 'Corretiva'
        # O diagrama também inclui 'PREDITIVA', vamos adicioná-la.
        PREDITIVA = 'PREDITIVA', 'Preditiva'

    class StatusManutencaoChoices(models.TextChoices):
        RASCUNHO = 'RASCUNHO', 'Rascunho'
        PROGRAMADA = 'PROGRAMADA', 'Programada'
        EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em Andamento'
        IMPEDIDA = 'IMPEDIDA', 'Impedida'
        EXECUTADA = 'EXECUTADA', 'Executada'

    # Relacionamento com Ativo
    ativo = models.ForeignKey(
        Ativo,
        on_delete=models.CASCADE,
        related_name='manutencoes_programadas',
        verbose_name="Ativo"
    )
    
    # Atributos do modelo ManutencaoProgramada
    data_programada = models.DateField(verbose_name="Data Programada")
    tipo_manutencao = models.CharField(
        max_length=15,
        choices=TipoManutencaoChoices.choices,
        verbose_name="Tipo de Manutenção"
    )
    # Assumindo que 'Serviço' é um texto descritivo por enquanto.
    # Se 'Serviço' fosse uma entidade separada com custo, etc., criaríamos outro modelo para ele.
    servico = models.CharField(max_length=255, verbose_name="Serviço a ser executado")
    status = models.CharField(
        max_length=15,
        choices=StatusManutencaoChoices.choices,
        default=StatusManutencaoChoices.RASCUNHO,
        verbose_name="Status"
    )
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return f"{self.servico} para {self.ativo.descricao} em {self.data_programada}"

    class Meta:
        verbose_name = "Manutenção Programada"
        verbose_name_plural = "Manutenções Programadas"


# Modelo OrdemServico
# Baseado na descrição textual e no Diagrama de Classe.
class OrdemServico(models.Model):
    """
    Registra as ordens de serviço executadas nos ativos, podendo ou não
    ter origem em uma manutenção programada.
    """
    # Relacionamento com Ativo
    ativo = models.ForeignKey(
        Ativo,
        on_delete=models.PROTECT, # Usar PROTECT para não apagar OS se o ativo for deletado
        related_name='ordens_servico',
        verbose_name="Ativo"
    )
    
    # Relacionamento opcional com ManutencaoProgramada
    manutencao_origem = models.ForeignKey(
        ManutencaoProgramada,
        on_delete=models.SET_NULL, # Se a programação for deletada, não apagar a OS
        null=True,
        blank=True,
        related_name='ordem_servico_executada',
        verbose_name="Manutenção de Origem"
    )
    
    # Atributos do modelo OrdemServico
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data de Abertura")
    servico = models.TextField(verbose_name="Serviço Executado")
    hodometro_atual = models.FloatField(verbose_name="Hodômetro na Execução")
    horimetro_atual = models.FloatField(verbose_name="Horímetro na Execução")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return f"OS para {self.ativo.descricao} em {self.data.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
        ordering = ['-data'] # Ordenar da mais recente para a mais antiga por padrão