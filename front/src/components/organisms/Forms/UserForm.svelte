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
  let selectDomain;

  /**
   * @type {any}
  */
  export let data;

  const user = data.user;
  const domains = data.domains;
  const domainsList = domains.map((/** @type {{ name: string; }} */ item) => item.name);
  const roles = data.roles;
  const rolesList = roles.map((/** @type {{ name: string; }} */ item) => item.name);
  const translations = data.translations;
  const translationsList = translations.map((/** @type {{ name: string; }} */ item) => item.name);

  let employeePicture = user.profile_picture;

  // TO CHANGER WHEN NASSIM FINISHED ENDPOINT
  let toChange = ["french"];
</script>

<form class="form-newUser" method="Post" action="?/register">

  <div class='avatar-upload block-center'>
    <Image
      imageSrc={employeePicture ? employeePicture : Account }
      imageAlt="Employee picture"
      imageWidth=80
      border
    />
    <br>
    <InputForm type='file' id='avatar' name='avatar'> 
      Importer image
    </InputForm>
  </div>

  <InputForm id='lastname' name='fullname' bind:valueInput={user.fullname} widthForm='calc(50% - 5px)'> Nom complet </InputForm>
  <InputForm id='email' name='email' type='email' bind:valueInput={user.email} widthForm='calc(50% - 5px)'> Email </InputForm>

  <SelectForm nameSelect="domain" options={domainsList} labelName='domain' widthForm='calc(50% - 5px)' bind:selectValue={user.domain} > Domaine </SelectForm>
  <SelectForm nameSelect="role" options={rolesList} labelName='role' widthForm='calc(50% - 5px)' bind:selectValue={user.role}> Rôle </SelectForm>
  
  {#if user.domain == 'translation'}
    <CheckboxForm data={translationsList} catForm='langues-traducteur' bind:optionsSelected={toChange}> Langues de traduction </CheckboxForm>
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