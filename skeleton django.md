Ótima pergunta! A "CLI" (Interface de Linha de Comando) do Django não é um pacote separado que você instala. Na verdade, ela é instalada automaticamente **junto com o próprio framework Django**.

A ferramenta principal que você usará é o `django-admin`. Para instalá-la, você só precisa instalar o Django usando o `pip`, o gerenciador de pacotes do Python.

Aqui está o guia completo e a maneira correta de fazer isso, utilizando as melhores práticas como ambientes virtuais.

---

### Passo a Passo para Instalar o Django e sua CLI

A melhor prática é instalar o Django em um "ambiente virtual" para cada projeto. Isso isola as dependências do seu projeto e evita conflitos com outros projetos ou com os pacotes Python do seu sistema.

#### Passo 1: Verifique os Pré-requisitos (Python e pip)

Antes de começar, garanta que você tenha o Python e o `pip` instalados. Abra seu terminal (Prompt de Comando, PowerShell, ou Terminal do Linux/macOS) e digite:

```bash
# Para verificar a versão do Python
python --version
# ou em alguns sistemas
python3 --version

# Para verificar a versão do pip
pip --version
# ou
pip3 --version
```

Se você não tiver o Python, baixe-o do site oficial [python.org](https://python.org). O `pip` geralmente já vem incluído nas versões mais recentes do Python.

#### Passo 2: Crie e Ative um Ambiente Virtual

1.  **Navegue até a pasta** onde você deseja criar seu projeto.
2.  **Crie o ambiente virtual.** Vamos chamá-lo de `venv` (um nome comum):

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual.** Este passo é crucial e varia conforme o seu sistema operacional:

    * **No Windows (Prompt de Comando ou PowerShell):**
        ```bash
        venv\Scripts\activate
        ```

    * **No macOS e Linux:**
        ```bash
        source venv/bin/activate
        ```

    Você saberá que o ambiente está ativo porque o nome dele, `(venv)`, aparecerá no início da linha do seu terminal.

#### Passo 3: Instale o Django

Agora que seu ambiente virtual está ativo, use o `pip` para instalar o Django.

```bash
pip install django
```

Este comando irá baixar e instalar a versão estável mais recente do Django e todas as suas dependências, incluindo a famosa ferramenta de linha de comando `django-admin`.

**Dica:** Para projetos em produção, é uma boa prática instalar uma versão específica do Django para garantir a consistência do ambiente:
```bash
# Exemplo instalando a versão 4.2 do Django
pip install django==4.2
```

#### Passo 4: Verifique a Instalação

Para confirmar que o Django e sua CLI foram instalados com sucesso, execute o seguinte comando:

```bash
django-admin --version
```

Se a instalação ocorreu corretamente, o terminal irá exibir a versão do Django que você acabou de instalar.

### Entendendo a "CLI" do Django: `django-admin` vs. `manage.py`

É importante entender que, após instalar o Django, você interagirá com duas ferramentas de linha de comando principais:

1.  `django-admin`:
    * É a ferramenta global que fica disponível assim que você instala o Django.
    * Você a utiliza principalmente para uma tarefa: **criar um novo projeto** com o comando `django-admin startproject nome_do_projeto`.

2.  `python manage.py`:
    * O arquivo `manage.py` é criado automaticamente **dentro do seu projeto** quando você usa o comando `startproject`.
    * Ele é um "wrapper" (um invólucro) do `django-admin` que já configura o ambiente para apontar para as configurações do seu projeto específico.
    * **Você usará `python manage.py` para a grande maioria das tarefas** dentro de um projeto, como:
        * `python manage.py runserver` (para iniciar o servidor de desenvolvimento)
        * `python manage.py startapp nome_da_app` (para criar uma nova aplicação)
        * `python manage.py migrate` (para aplicar migrações ao banco de dados)
        * `python manage.py createsuperuser` (para criar um usuário administrador)

### Resumo Rápido

| Ação                                     | Comando                                   | Quando Usar                                     |
| ---------------------------------------- | ----------------------------------------- | ----------------------------------------------- |
| **Instalar a CLI do Django** | `pip install django`                      | Dentro de um ambiente virtual ativo.            |
| **Criar um novo projeto** | `django-admin startproject meuprojeto`    | Para iniciar a estrutura de um projeto do zero. |
| **Gerenciar um projeto existente** | `python manage.py <comando>`              | Para todas as outras tarefas dentro do projeto. |