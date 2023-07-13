<script>
  import Button from "../../atoms/Button.svelte";
  import Text from "../../atoms/Text.svelte";
  import SelectForm from "../../molecules/formFields/SelectForm.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";
  import Image from "../../atoms/Image.svelte";
  import Icon from "../../atoms/Icon.svelte";
  import AddIcon from "../../../assets/icons/AddIcon.svelte";

  import Account from "../../../assets/img/account.png";

  /**
   * @type {string}
  */
  export let selectRole;
  /**
   * @type {string}
   */
   export let selectDomain;

  /**
   * @type {any}
  */
  export let employeePicture = '';

    /**
   * @type {any}
  */
  export let data;
  
  let domainList = [{ id:1, name:'traducteur'}, {id:2, name:'regisseur'}, {id:3, name:'editeur'}];
  let roleList = [{ id:1, name:'admin'}, {id:2, name:'superadmin'}, {id:3, name:'user'}];
  let translationsList = [{ id:1, name:'anglais'}, {id:2, name:'espagnol'}, {id:3, name:'allemand'}, { id:1, name:'italien'}, {id:2, name:'russe'}, {id:3, name:'japonais'}];
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

  <InputForm id='lastname' name='fullname' widthForm='calc(50% - 5px)'> Nom complet </InputForm>
  <InputForm id='email' name='email' type='email' widthForm='calc(50% - 5px)'> Email </InputForm>
  <InputForm id='password' name='password'> Mot de passe </InputForm>
  <SelectForm nameSelect="domain" data={domainList} labelName='domain' widthForm='calc(50% - 5px)' bind:selectValue={selectRole} > Domaine </SelectForm>
  <SelectForm nameSelect="role" data={roleList} labelName='role' widthForm='calc(50% - 5px)' bind:selectValue={selectDomain}> Rôle </SelectForm>
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