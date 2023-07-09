<script>
  import Text from '../../../components/atoms/Text.svelte';
  import Tabs from '../../../components/molecules/Tabs.svelte';

  import Tab1 from "../../../tabs/validation-montage.svelte";
  import Tab2 from "../../../tabs/validation-finale.svelte";
  import Tab3 from "../../../tabs/encours-superadmin.svelte";

  export let data;

  let items = [
    { label: "Validation montage",
     value: 1,
     component: Tab1
    },
    { label: "Validation finale",
     value: 2,
     component: Tab2
    },
    { label: "En cours",
     value: 3,
     component: Tab3
    }
  ];
</script>

<div class='card block-center'>
  <Text
    textTag='h1'
    class='text-preset-1 text-center text--uppercase'
    >
    Les projets
  </Text>

  <div class='dashboard-nav'>
    <Tabs {items} data={data}/>
  </div>

</div>

<style>
  .dashboard-nav{
    position: relative;
    margin-top: var(--spacing-5);
  }
</style>