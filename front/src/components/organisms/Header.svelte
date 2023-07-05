<script>
  import Image from "../atoms/Image.svelte";
  import Logo from '../../assets/img/logo_color.png'
  import Account from "../../assets/img/account.png";
  import Link from "../atoms/Link.svelte";

  /**
   * @type {string}
  */
  export let role = 'superadmin';
  export let domain = 'Traducteur';
  export let current = 'home';

  /**
  * @type {string | undefined}
  */
   export let employeePicture;
   
</script>

<div class='header'>
  <Image
    imageSrc={Logo}
    imageAlt="Saline Academie Logo"
    imageWidth=160
  />

  <ul class='nav'>
    {#if role == 'superadmin' || role == 'admin' && domain == 'Traducteur'}
      <Link
        class='text--uppercase text--semibold {current === 'home' ? 'link--current' : ''}'
        linkUrl='/dashboard'
        linkStyle='padding: 0 var(--spacing-3);'
        linkColor='{current === 'home' ? 'blue' : 'grey'}'
      > 
        Les projets
      </Link>

      <Link
        class='text--uppercase text--semibold'
        linkUrl='/dashboard'
        linkStyle='padding: 0 var(--spacing-3);'
        linkColor='grey'
      >
        Vidéos en ligne
      </Link>
    {/if}
    
    {#if role == 'superadmin'}
      <Link
        class='text--uppercase text--semibold'
        linkUrl='/dashboard'
        linkStyle='padding: 0 var(--spacing-3);'
        linkColor='grey'
      > 
        Les utilisateurs
      </Link>
    {/if}

    {#if role == 'admin' && domain == 'Regisseur'}
      <Link
        class='text--uppercase text--semibold'
        linkUrl='/dashboard-admin-regi'
        linkStyle='padding: 0 var(--spacing-3);'
        linkColor='grey'
      > 
        Mes projets
      </Link>

      <Link
        class='text--uppercase text--semibold'
        linkUrl='/dashboard-regi'
        linkStyle='padding: 0 var(--spacing-3);'
        linkColor='grey'
      > 
        Projets équipe
      </Link>
    {/if}
  </ul>

  <Image
    imageSrc={employeePicture ? employeePicture : Account }
    imageAlt="Employee picture"
    imageWidth=50
    border
  />
</div>

<style>
  .header{
    display: flex;
    margin: var(--spacing-3) var(--spacing-5);
    align-items: center;
    column-gap: var(--spacing-3);
  }

  .nav{
    width: calc(100% - 210px);
    display: flex;
    justify-content: end;
  }
</style>