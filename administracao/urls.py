from django.urls import path
from .views import servicos_views, usuario_views
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy


app_name = 'administracao'

urlpatterns = [
    path('servicos/cadastrar/', servicos_views.cadastrar_servico, 
         name='cadastrar_servico'),
    path('servicos/listar/', servicos_views.listar_servicos, 
         name='listar_servicos'),
    path('servico/editar/<int:id>/', servicos_views.editar_servico, 
         name='editar_servico'),

    path('usuario/cadastrar/', usuario_views.cadastrar_usuario, 
         name='cadastrar_usuario'),
    path('usuario/listar', usuario_views.listar_usuarios, 
         name='listar_usuarios'),
    path('usuario/editar/<int:id>', usuario_views.editar_usuario, 
         name='editar_usuario'),

    path('autenticacao/login/', auth_views.LoginView.as_view(), 
         name='logar_usuario'),
    path('autenticacao/logout/', auth_views.LogoutView.as_view(), 
         name='deslogar_usuario'),

    path('alterar_senha', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('administracao:listar_servicos')
        ), name='alterar_senha'),
    path('resetar_senha/', auth_views.PasswordResetView.as_view(), 
         name='resetar_senha'),
    path('resetar_senha/sucesso/', auth_views.PasswordResetDoneView.as_view(), 
         name='resetar_senha_sucesso'),
    path('resetar_senha/<str:uid64>/<str:token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='resetar_senha_confirmar'),
    path('resetar_senha/feito/', auth_views.PasswordResetDoneView.as_view(), 
         name='resetar_senha_feito'),
]