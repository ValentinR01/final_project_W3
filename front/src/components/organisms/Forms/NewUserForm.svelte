<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";
  import Image from "../../atoms/Image.svelte";

  import Account from "../../../assets/img/account.png";

  /**
   * @type {string}
  */
  let selectRole;

  /**
   * @type {string}
  */
  let selectDomain;

  /**
   * @type {any}
  */
  export let data;

  const domains = data.domains; 
  const domainsList = domains.map((/** @type {{ name: string; }} */ item) => item.name);
  const roles = data.roles;
  const rolesList = roles.map((/** @type {{ name: string; }} */ item) => item.name);
  const translations = data.translations;
  const translationsList = translations.map((/** @type {{ name: string; }} */ item) => item.name);
</script>

<form class="form-newUser" method="Post" action="?/register"> 
  <Text
    textTag='h1'
    class='text-preset-1 text--uppercase w-100 text-center'
  > 
    Nouvel utilisateur
  </Text>

  <div class='avatar-upload block-center'>
    <Image
      imageSrc={Account}
      imageAlt="Employee picture"
      imageWidth=80
      border
    />
    <br>
    <InputForm type='file' id='avatar' name='avatar'> 
      Importer image
    </InputForm>
  </div>

  <InputForm id='lastname' name='fullname' widthForm='calc(50% - 5px)' required> Nom complet </InputForm>
  <InputForm id='email' name='email' type='email' widthForm='calc(50% - 5px)' required> Email </InputForm>
  <InputForm id='password' name='password' type='password' required> Mot de passe </InputForm>

  <SelectForm nameSelect="domain" options={domainsList} labelName='domain' widthForm='calc(50% - 5px)' bind:selectValue={selectDomain} > Domaine </SelectForm>
  <SelectForm nameSelect="role" options={rolesList} labelName='role' widthForm='calc(50% - 5px)' bind:selectValue={selectRole}> Rôle </SelectForm>
  
  {#if selectDomain == 'traducteur'}
    <CheckboxForm data={translationsList} catForm='langues-traducteur'> Langues de traduction </CheckboxForm>
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

  .avatar-upload{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .avatar-upload :global(.input-form){
    width: auto;
    text-align: center;
    margin-top: var(--spacing-1);
  }
</style>