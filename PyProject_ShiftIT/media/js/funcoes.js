$(document).ready
(
	function()
	{
		
	//------------------------------Eventos------------------------------
		
		if (window.location.pathname == "/")
		{
			
			$('#contatoTel').keypress(permitirApenasNumeros('#contatoTel'));
		
		}
		
		if (window.location.pathname == "/contato/")
		{
		
			$('#contatoTel').keypress(permitirApenasNumeros('#contatoTel'));
		
		}
		if (window.location.pathname == "/seuprojeto/")
		{
		
			$('#id_telefone').keypress(permitirApenasNumeros('#id_telefone'));
		
		}
		
	}
);


//------------------------------Funcoes------------------------------


function permitirApenasNumeros(vCampoID)
{
	$(vCampoID).numeric();
}
