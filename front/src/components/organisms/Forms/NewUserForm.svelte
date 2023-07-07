<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";
  
  /**
   * @type {any}
  */
  export let data;

  export let selectValue;

</script>

<form class="form-newUser">
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase w-100 text-center'
  > 
    Nouvel utilisateur
  </Text>

  <InputForm id='lastname' name='lastname' widthForm='calc(50% - 5px)'> Nom </InputForm>
  <InputForm id='firstname' name='firstname' widthForm='calc(50% - 5px)'> Prénom </InputForm>
  <InputForm id='email' name='email'> Email </InputForm>
  <SelectForm nameSelect="domain" data={data.metadata.domain} labelName='domain' widthForm='calc(50% - 5px)' bind:selectValue={selectValue} > Domaine </SelectForm>
  <SelectForm nameSelect="role" data={data.metadata.role} labelName='role' widthForm='calc(50% - 5px)' > Rôle </SelectForm>
  {#if selectValue == 'traducteur'}
    <CheckboxForm data={data.metadata.translations} catForm='langues-traducteur'> Langues de traduction </CheckboxForm>
  {/if}
  <Button marginTop='var(--spacing-2)'> Valider </Button>
</form>

<style>
  .form-newUser{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    row-gap: var(--spacing-3);
    column-gap: var(--spacing-2);
  }
</style>