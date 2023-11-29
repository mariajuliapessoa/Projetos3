import imp
from rolepermissions.roles import AbstractUserRole

class Usuario(AbstractUserRole):
    available_permissions = {
    'cadastrar_como_usuario_comum': True,
    'cadastrar_como_voluntario_projeto': True,
    'solicitar_credenciamento_embaixador': True,
	'realizar_doacao_projeto_existente': True,
	'visualizar_infos': True,
	'visualizar_projetos_disponiveis': True,
	'visualizar_atualizacoes_projeto': True,
	'visualizar_infos_contato_projeto': True,
	'visualizar_relatorios_atividades_ONGs': True,
	'visualizar_perfis_embaixadores': True,
	'filtro_localidade': True,
	'filtrar_projeto_por_localidade': True,
	'filtrar_perfil_embaixadores_localidade': True
    }

class Gerente(AbstractUserRole):
    available_permissions = {
        'armazenar_dados': True,
	'armazenar_projetos': True,
	'armazenar_voluntarios': True,
	'armazenar_doacoes': True,
	'armazenar_relatorios_semanais': True,
	'admitir_entidades_na_plataforma': True,
	'admitir_projetos': True,
	'admitir_embaixadores': True,
	'visualizar_dados': True,
	'visualizar_cadastro_dos_usuarios': True,
	'dados_usuarios_comuns': True,
	'visualizar_cadastro_projetos': True,
	'visualizar_relatorios_semestrais': True,
	'visualizar_doacoes': True,
    }

class Embaixador(AbstractUserRole):
    available_permissions = {
	'visualizar_info_cadastro':True,
	'visualizar_pedidos_cadastro_projeto':True,
	'visualizar_validacao_atribuida_outro_embaixador':True,
	'visualizar_todos_projetos_cadastrados':True,
	'divulgar_dados_redes_sociais':True,
	'expor_projetos_embaixador_guia':True,
	'divulgar_interesse_ajudar':True,
	'filtro_localidade':True,
	'aplicar_filtro_projetos_desejam_cadastrado':True,
	'sinalizar_responsabilidade_validacao_pedido_cadastro':True,
}

class DonoProjeto(AbstractUserRole):
    available_permissions = {
	'cadastrar_infos': True,
	'cadastrar_projeto': True,
	'personalizar_pag_inicial': True,
	'cadastrar_voluntarios': True,
	'cadastrar_demandas': True,
	'visualizar_infos':True,
	'visualizar_dados_voluntarios_cadastrados':True,
	'visualizar_dados_voluntarios_inscritos':True,
	'aprovar_usuario':True,
	'visualizar_dados_doacoes':True,
	'editar_info':True,
	'editar_pag_principal_projeto':True,
	'editar_voluntarios_cadastrados':True,
	'editar_demandas':True,
}