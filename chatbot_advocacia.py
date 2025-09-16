import re
import datetime

class ChatbotAdvocacia:
    def __init__(self):
        self.nome_escritorio = "Consultório Jurídico Silva & Associados"
        self.telefone = "(11) 9999-9999"
        self.email = "contato@silvaadvocacia.com.br"
        self.endereco = "Rua das Flores, 123 - Centro - São Paulo/SP"
        self.horario_funcionamento = "Segunda a Sexta: 8h às 18h"
        
        # Base de conhecimento com perguntas frequentes
        self.faq = {
            "honorarios": "Nossos honorários variam conforme a complexidade do caso. Oferecemos consulta inicial gratuita para avaliar sua situação.",
            "areas": "Atuamos nas seguintes áreas: Direito Civil, Direito Trabalhista, Direito de Família, Direito Empresarial e Direito do Consumidor.",
            "consulta": "Para agendar uma consulta, entre em contato pelo telefone (11) 9999-9999 ou pelo email contato@silvaadvocacia.com.br",
            "documentos": "Para a primeira consulta, traga RG, CPF e todos os documentos relacionados ao seu caso (contratos, comprovantes, etc.).",
            "prazo": "Os prazos variam conforme o tipo de processo. Durante a consulta, explicaremos os prazos específicos do seu caso.",
            "online": "Sim, oferecemos consultas online via videoconferência. Entre em contato para agendar."
        }
        
        # Padrões de reconhecimento de intenções
        self.padroes = {
            "saudacao": [r"oi", r"olá", r"bom dia", r"boa tarde", r"boa noite", r"hello", r"alo"],
            "despedida": [r"tchau", r"até logo", r"obrigado", r"obrigada", r"bye", r"adeus"],
            "honorarios": [r"quanto custa", r"preço", r"valor", r"honorário", r"custo"],
            "areas": [r"área", r"especialidade", r"tipo", r"ramo", r"direito"],
            "consulta": [r"agendar", r"marcar", r"consulta", r"atendimento", r"horário"],
            "documentos": [r"documento", r"papel", r"levar", r"trazer", r"preciso"],
            "prazo": [r"prazo", r"tempo", r"demora", r"quanto tempo"],
            "contato": [r"telefone", r"email", r"endereço", r"localização", r"onde"],
            "online": [r"online", r"virtual", r"videoconferência", r"remoto", r"distância"]
        }

    def processar_mensagem(self, mensagem):
        """Processa a mensagem do usuário e retorna uma resposta apropriada"""
        mensagem = mensagem.lower().strip()
        
        # Verifica padrões de intenção
        for intencao, padroes in self.padroes.items():
            for padrao in padroes:
                if re.search(padrao, mensagem):
                    return self.gerar_resposta(intencao)
        
        # Se não encontrou padrão específico, retorna resposta padrão
        return self.resposta_padrao()

    def gerar_resposta(self, intencao):
        """Gera resposta baseada na intenção identificada"""
        respostas = {
            "saudacao": f"Olá! Bem-vindo ao {self.nome_escritorio}! 👋\n\nComo posso ajudá-lo hoje? Posso fornecer informações sobre:\n• Nossas áreas de atuação\n• Agendamento de consultas\n• Honorários\n• Documentos necessários\n• Contato",
            
            "despedida": "Obrigado por entrar em contato conosco! 😊\n\nSe precisar de mais informações, não hesite em nos procurar.\n\nTenha um ótimo dia!",
            
            "honorarios": f"💰 **Honorários**\n\n{self.faq['honorarios']}\n\nPara mais informações:\n📞 {self.telefone}\n📧 {self.email}",
            
            "areas": f"⚖️ **Áreas de Atuação**\n\n{self.faq['areas']}\n\nCada área tem suas particularidades. Agende uma consulta para discutirmos seu caso específico!",
            
            "consulta": f"📅 **Agendamento de Consulta**\n\n{self.faq['consulta']}\n\n🕐 {self.horario_funcionamento}\n📍 {self.endereco}",
            
            "documentos": f"📋 **Documentos Necessários**\n\n{self.faq['documentos']}\n\nDica: Organize os documentos cronologicamente para facilitar a análise do caso.",
            
            "prazo": f"⏰ **Prazos Processuais**\n\n{self.faq['prazo']}\n\nLembre-se: prazos judiciais são improrrogáveis. Entre em contato o quanto antes!",
            
            "contato": f"📞 **Informações de Contato**\n\n🏢 {self.nome_escritorio}\n📞 Telefone: {self.telefone}\n📧 Email: {self.email}\n📍 Endereço: {self.endereco}\n🕐 Horário: {self.horario_funcionamento}",
            
            "online": f"💻 **Consultas Online**\n\n{self.faq['online']}\n\nAs consultas online têm a mesma qualidade das presenciais, com total sigilo e segurança."
        }
        
        return respostas.get(intencao, self.resposta_padrao())

    def resposta_padrao(self):
        """Resposta padrão quando não consegue identificar a intenção"""
        return f"""🤖 Desculpe, não entendi sua pergunta completamente.

Posso ajudá-lo com informações sobre:

⚖️ **Áreas de atuação** - Digite "areas"
📅 **Agendamento** - Digite "consulta" 
💰 **Honorários** - Digite "preço"
📋 **Documentos** - Digite "documentos"
⏰ **Prazos** - Digite "prazo"
📞 **Contato** - Digite "contato"
💻 **Consulta online** - Digite "online"

Ou entre em contato diretamente:
📞 {self.telefone}
📧 {self.email}"""

    def iniciar_conversa(self):
        """Inicia a conversa com o chatbot"""
        print("=" * 60)
        print(f"🏛️  {self.nome_escritorio.upper()}")
        print("=" * 60)
        print("Chatbot Jurídico - Assistente Virtual")
        print("Digite 'sair' para encerrar a conversa")
        print("=" * 60)
        
        while True:
            try:
                mensagem_usuario = input("\n👤 Você: ").strip()
                
                if mensagem_usuario.lower() in ['sair', 'exit', 'quit']:
                    print("\n🤖 Chatbot:", self.gerar_resposta("despedida"))
                    break
                
                if not mensagem_usuario:
                    print("\n🤖 Chatbot: Por favor, digite sua mensagem.")
                    continue
                
                resposta = self.processar_mensagem(mensagem_usuario)
                print(f"\n🤖 Chatbot: {resposta}")
                
            except KeyboardInterrupt:
                print("\n\n🤖 Chatbot:", self.gerar_resposta("despedida"))
                break
            except Exception as e:
                print(f"\n🤖 Chatbot: Desculpe, ocorreu um erro. Tente novamente.")

def main():
    """Função principal para executar o chatbot"""
    chatbot = ChatbotAdvocacia()
    chatbot.iniciar_conversa()

if __name__ == "__main__":
    main()
