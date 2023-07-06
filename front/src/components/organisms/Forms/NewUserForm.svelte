<script>
  import Button from "../../atoms/Button.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";
  
  /**
   * @type {any}
  */
  export let data;

</script>

<form class="form-newUser">
  <InputForm widthForm='calc(50% - 5px)'> Nom </InputForm>
  <InputForm widthForm='calc(50% - 5px)'> Prénom </InputForm>
  <InputForm> Email </InputForm>
  <SelectForm nameSelect="domain" data={data.metadata.domain} labelName='domain' widthForm='calc(50% - 5px)' > Domaine </SelectForm>
  <SelectForm nameSelect="role" data={data.metadata.role} labelName='role' widthForm='calc(50% - 5px)' > Rôle </SelectForm>
  <CheckboxForm data={data.metadata.translations} catForm='langues-traducteur'> Langues de traduction </CheckboxForm>
  <Button marginTop='var(--spacing-4)'> Valider </Button>
</form>

<style>
  .form-newUser{
    display: flex;
    flex-wrap: wrap;
    justify-content: end;
    row-gap: var(--spacing-2);
    column-gap: var(--spacing-2);
  }
</style>