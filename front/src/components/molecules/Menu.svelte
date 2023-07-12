<script>
  import Link from "../atoms/Link.svelte";

  /**
   * @type {string}
  */
  export let currentPage = 'home';
  export let role = 'superadmin';
  export let domain = 'traducteur';

</script>

<!-- REVOIR LES REDIRECTIONS APRES CREATION PAGES & RECUPERATION DES ROLES DEPUIS LA BDD -->

<ul class='nav'>
  {#if role == 'superadmin' || role == 'admin' && domain == 'traducteur'}
    <Link
      class='text--uppercase text--semibold {currentPage === 'home' ? 'link--current' : ''}'
      linkUrl='projects/dashboard'
      linkStyle='padding: 0 var(--spacing-3);'
      linkColor='{currentPage === 'home' ? 'blue' : 'grey'}'
    > 
      Les projets
    </Link>

    <Link
      class='text--uppercase text--semibold'
      linkUrl='/projects/online'
      linkStyle='padding: 0 var(--spacing-3);'
      linkColor='grey'
    >
      Vidéos en ligne
    </Link>
  {/if}
  
  {#if role == 'superadmin'}
    <Link
      class='text--uppercase text--semibold'
      linkUrl='/users/dashboard'
      linkStyle='padding: 0 var(--spacing-3);'
      linkColor='grey'
    > 
      Les utilisateurs
    </Link>
  {/if}

  {#if role == 'admin' && domain == 'regisseur'}
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

<style>
  .nav{
    width: calc(100% - 210px);
    display: flex;
    justify-content: end;
  }
</style>