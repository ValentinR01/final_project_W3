<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import Margin from "../../atoms/Margin.svelte";

  export let form;
</script>

<form method="POST" action="?/login" class="login-form block-center">
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase w-100 text-center'
  > 
    Identification
  </Text>

  <InputForm id='username' name='username' type="email" valueInput="{form?.username || ""}" required> Username </InputForm>
  <Margin marginTop="var(--spacing-2)">
    <InputForm id='password' name='password' type="password" required> Password </InputForm>
  </Margin>

  <Button marginTop='var(--spacing-3)' class="block-center"> Valider </Button>
</form>

{#if form?.message}
  <Margin marginTop="-80px">
    <Text textTag='p' textColor='blue' class="text-preset-3 text-center error">{form.message}</Text>
  </Margin>
{/if}

<style>
  .login-form{
    width: 300px;
    margin-top: 50%;
    transform: translateY(-50%);
  }
</style>