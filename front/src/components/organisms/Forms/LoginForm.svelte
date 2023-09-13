<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
</script>

<form method="POST" class="login-form block-center">
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase w-100 text-center'
  > 
    Identification
  </Text>

  <InputForm id='username' name='username'> Username </InputForm>
  <InputForm id='password' name='password'> Password </InputForm>

  <Button marginTop='var(--spacing-3)' class="block-center"> Valider </Button>
</form>

<style>
  .login-form{
    width: 300px;
    margin-top: 50%;
    transform: translateY(-50%);
  }
</style>