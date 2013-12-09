$(document).ready
(
	function()
	{
		
	//------------------------------Eventos------------------------------
		
		if (window.location.pathname == "/")
		{
			
			$('#contatoTel').keypress(permitirApenasNumeros('#contatoTel'));
			$('#contatoTel').keypress(permitirApenasNumeros('#contatoTel'));
		
		}
		
		if (window.location.pathname == "/contato/")
		{
		
			$('#contatoTel').keypress(permitirApenasNumeros('#contatoTel'));
			$('#contatoTel').keypress(permitirApenasNumeros('#contatoTel'));
		
		}
		
	}
);


//------------------------------Funcoes------------------------------


function permitirApenasNumeros(vCampoID)
{
	$(vCampoID).numeric();
}
